# Copyright 2020 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Rigid-body transformations including velocities and static forces."""

# pylint: disable=unused-import
from transformations._transformations import (
    axisangle_to_euler,
    axisangle_to_quat,
    axisangle_to_rmat,
    cross_2d,
    cross_mat_from_vec3,
    euler_to_axisangle,
    euler_to_quat,
    euler_to_rmat,
    force_transform,
    force_transform_2d,
    hmat_inv,
    hmat_to_pos_quat,
    hmat_to_poseuler,
    hmat_to_twist,
    integrate_hmat,
    integrate_quat,
    mat_to_quat,
    matrix_to_postheta_2d,
    pos_quat_to_hmat,
    pos_to_hmat,
    poseuler_to_hmat,
    positive_leading_quat,
    postheta_to_matrix_2d,
    quat_angle,
    quat_axis,
    quat_between_vectors,
    quat_conj,
    quat_diff_active,
    quat_diff_passive,
    quat_dist,
    quat_exp,
    quat_inv,
    quat_log,
    quat_mul,
    quat_rotate,
    quat_slerp,
    quat_to_axisangle,
    quat_to_euler,
    quat_to_mat,
    rmat_to_axisangle,
    rmat_to_euler,
    rmat_to_hmat,
    rmat_to_rot6,
    rot6_to_rmat,
    rotate_vec6,
    rotation_matrix_2d,
    rotation_x_axis,
    rotation_y_axis,
    rotation_z_axis,
    twist_to_hmat,
    velocity_transform,
    velocity_transform_2d,
)

# pytype: disable=import-error
# pylint: disable=g-import-not-at-top,reimported
try:
  # Use faster C extension versions if _transformations_quat is available.
  from transformations._transformations_quat import (
      axisangle_to_quat,
      hmat_to_pos_quat,
      integrate_quat,
      mat_to_quat,
      pos_quat_to_hmat,
      quat_angle,
      quat_conj,
      quat_dist,
      quat_exp,
      quat_inv,
      quat_log,
      quat_mul,
      quat_rotate,
      quat_slerp,
      quat_to_mat,
  )

  # TODO(benmoran) Consider quaternion implementations of other functions:
  # from transformations._transformations import quat_axis
  # from transformations._transformations \
  #  import quat_between_vectors
  # from transformations._transformations import quat_diff_active
  # from transformations._transformations import quat_diff_passive
  # from transformations._transformations import quat_to_axisangle
  # from transformations._transformations import quat_to_euler
  HAVE_NUMPY_QUATERNION = True
except ImportError:
  HAVE_NUMPY_QUATERNION = False
# pytype: enable=import-error
# pylint: enable=g-import-not-at-top,reimported
