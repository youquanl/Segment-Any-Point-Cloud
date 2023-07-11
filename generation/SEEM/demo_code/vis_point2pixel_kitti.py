import cv2
import numpy as np
import os.path as osp




def select_points_in_frustum(points_2d, x1, y1, x2, y2):
    """
    Select points in a 2D frustum parametrized by x1, y1, x2, y2 in image coordinates
    :param points_2d: point cloud projected into 2D
    :param points_3d: point cloud
    :param x1: left bound
    :param y1: upper bound
    :param x2: right bound
    :param y2: lower bound
    :return: points (2D and 3D) that are in the frustum
    """
    keep_ind = (points_2d[:, 0] > x1) * \
               (points_2d[:, 1] > y1) * \
               (points_2d[:, 0] < x2) * \
               (points_2d[:, 1] < y2)

    return keep_ind

def read_calib(calib_path):
    """
    :param calib_path: Path to a calibration text file.
    :return: dict with calibration matrices.
    """
    calib_all = {}
    with open(calib_path, 'r') as f:
        for line in f.readlines():
            if line == '\n':
                break
            key, value = line.split(':', 1)
            calib_all[key] = np.array([float(x) for x in value.split()])

    # reshape matrices
    calib_out = {}
    calib_out['P2'] = calib_all['P2'].reshape(3, 4)  # 3x4 projection matrix for left camera
    calib_out['Tr'] = np.identity(4)  # 4x4 matrix
    calib_out['Tr'][:3, :4] = calib_all['Tr'].reshape(3, 4)

    return calib_out




ann_info = "./vis_samples_kitti/dataset/sequences/18/velodyne/000000.bin"
points = np.fromfile(ann_info, dtype=np.float32).reshape((-1, 4))
points = points[:,:3]
image_path = "./vis_samples_kitti/dataset/sequences/18/image_2/000000.png"
image = cv2.imread(image_path)
calib = read_calib("./vis_samples_kitti/dataset/sequences/18/calib.txt")
proj_matrix = calib['P2'] @ calib['Tr']
proj_matrix = proj_matrix.astype(np.float32)
# project points into image
keep_idx = points[:, 0] > 0  # only keep point in front of the vehicle
points_hcoords = np.concatenate([points, np.ones([len(points), 1], dtype=np.float32)], axis=1)
# points_hcoords = np.concatenate([points[keep_idx], np.ones([keep_idx.sum(), 1], dtype=np.float32)], axis=1)
img_points = (proj_matrix @ points_hcoords.T).T
img_points = img_points[:, :2] / np.expand_dims(img_points[:, 2], axis=1)  # scale 2D points

# print(img_points)
keep_idx_img_pts = select_points_in_frustum(img_points, 0, 0, 1241, 376)
keep_idx = keep_idx_img_pts & keep_idx
img_points = img_points[keep_idx]


points_h = points[keep_idx]

# cv2.namedWindow('win', cv2.WINDOW_NORMAL)
for  i in range(len(img_points)):
        cv2.circle(image, (int(img_points[i][0]), int(img_points[i][1])), 1, (255,255,0), -1)

cv2.imwrite('./2d_3d_projection.png',image)
# cv2.imshow('win',image)
# cv2.waitKey(60000)