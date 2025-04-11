# Transformations

![Tests](https://github.com/Reimagine-Robotics/transformations/actions/workflows/test.yml/badge.svg)
[![PyPI version](https://img.shields.io/pypi/v/r2-transformations.svg)](https://pypi.org/project/r2-transformations/)
[![License](https://img.shields.io/pypi/l/r2-transformations.svg)](https://github.com/Reimagine-Robotics/transformations/blob/main/LICENSE)

Forked version of the
[DeepMind Robotics `transformations` library][dm_robotics-transformations]
which makes the JAX dependency optional, for lighterweight setups.

Transformations is a pure Python library for rigid-body transformations,
including velocities and forces.

The objectives for this library are **simplicity** and **comprehensiveness**
across all canonical representations (euler, axis-angle, quaternion,
homogeneous matrices).

## Quick start

```shell
pip install r2-transformations
```

```python
from transformations import transformations as tr

# Convert a pose, euler angle into a homogeneous matrix (a 4x4 matrix):
hmat = tr.poseuler_to_hmat(
        np.array([x, y, z, rot_x, rot_y, rot_z]), 'XYZ')

# Convert the homogeneous matrix to a twist (a 6 vector):
twist = tr.hmat_to_twist(hmat)
```

For JAX use-cases:

```shell
pip install r2-transformations[jax]
```

```python
from transformations.jax_transformations import transformations as jax_tr

mat = jax_tr.quat_to_mat(quat)
jax_tr.hmat_to_twist(hmat)
```

See the files for the full list of functions available.

## Supported conversions

*   Quaternion to Rotation matrix, Axis-angle and Euler-angle
*   Axis-angle to Quaternion, Rotation matrix and Euler-angle
*   Rotation matrix to Quaternion, Axis-angle and Euler-angle
*   Euler-angle to Quaternion, Rotation matrix and Axis-angle

## Quaternions

Quaternions are represented with the scalar part (w) first, e.g.

```python
identity_quaternion = np.asarray([1, 0, 0, 0])  # w, i, j, k
```

Supported quaternion operations:

*   Difference
*   Distance
*   Multiplication
*   Inverse
*   Conjugate
*   Logarithm and Exponent
*   Slerp (spherical linear interpolation)
*   Rotation of a vector by a quaternion.

## Euler-angles

All 24 from-euler orderings are supported.
7 of 24 to-euler orderings are supported.

## Transforms

This library supports force and velocity transforms.

[dm_robotics-transformations]: <https://github.com/google-deepmind/dm_robotics/tree/main/py/transformations>
