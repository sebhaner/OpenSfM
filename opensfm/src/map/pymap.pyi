# Autogenerated by pybind stub generator
# Do not manually edit
# To regenerate:
#   $ buck run //mapillary/opensfm/opensfm/src/map:pymap_stubgen
# Use proper mode, e.g. @arvr/mode/linux/dev for arvr
# @generated

import numpy
import opensfm.pygeo
import opensfm.pygeometry
from typing import *
__all__  = [
"BiasView",
"CameraView",
"ErrorType",
"GroundControlPoint",
"GroundControlPointObservation",
"Landmark",
"LandmarkView",
"Map",
"Observation",
"PanoShotView",
"RigCamera",
"RigCameraView",
"RigInstance",
"RigInstanceView",
"Shot",
"ShotMeasurementDouble",
"ShotMeasurementInt",
"ShotMeasurementString",
"ShotMeasurementVec3d",
"ShotMeasurements",
"ShotMesh",
"ShotView",
"TracksManager",
"Angular",
"Normalized",
"Pixel"
]
class BiasView:
    def __contains__(self, arg0: str) -> bool: ...
    def __getitem__(self, arg0: str) -> opensfm.pygeometry.Similarity: ...
    def __init__(self, arg0: Map) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def get(self, arg0: str) -> opensfm.pygeometry.Similarity: ...
    def items(self) -> Iterator: ...
    def keys(self) -> Iterator: ...
    def values(self) -> Iterator: ...
class CameraView:
    def __contains__(self, arg0: str) -> bool: ...
    def __getitem__(self, arg0: str) -> opensfm.pygeometry.Camera: ...
    def __init__(self, arg0: Map) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def get(self, arg0: str) -> opensfm.pygeometry.Camera: ...
    def items(self) -> Iterator: ...
    def keys(self) -> Iterator: ...
    def values(self) -> Iterator: ...
class ErrorType:
    Pixel: "ErrorType"
    Normalized: "ErrorType"
    Angular: "ErrorType"
    __members__: Dict[str, "ErrorType"]
    @property
    def name(self) -> str: ...
class GroundControlPoint:
    def __init__(self) -> None: ...
    def add_observation(self, arg0: GroundControlPointObservation) -> None: ...
    @property
    def has_altitude(self) -> bool:...
    @has_altitude.setter
    def has_altitude(self, arg0: bool) -> None:...
    @property
    def id(self) -> str:...
    @id.setter
    def id(self, arg0: str) -> None:...
    @property
    def lla(self) -> Dict[str, float]:...
    @lla.setter
    def lla(self, arg0: Dict[str, float]) -> None:...
    @property
    def lla_vec(self) -> numpy.ndarray:...
    @lla_vec.setter
    def lla_vec(self, arg1: float, arg2: float, arg3: float) -> None:...
    @property
    def observations(self) -> List[GroundControlPointObservation]:...
    @observations.setter
    def observations(self, arg1: List[GroundControlPointObservation]) -> None:...
class GroundControlPointObservation:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: numpy.ndarray) -> None: ...
    @property
    def projection(self) -> numpy.ndarray:...
    @projection.setter
    def projection(self, arg0: numpy.ndarray) -> None:...
    @property
    def shot_id(self) -> str:...
    @shot_id.setter
    def shot_id(self, arg0: str) -> None:...
class Landmark:
    def __init__(self, arg0: str, arg1: numpy.ndarray) -> None: ...
    def get_observations(self) -> Dict[Shot, int]: ...
    def number_of_observations(self) -> int: ...
    @property
    def color(self) -> numpy.ndarray:...
    @color.setter
    def color(self, arg1: numpy.ndarray) -> None:...
    @property
    def coordinates(self) -> numpy.ndarray:...
    @coordinates.setter
    def coordinates(self, arg1: numpy.ndarray) -> None:...
    @property
    def id(self) -> str:...
    @property
    def reprojection_errors(self) -> Dict[str, numpy.ndarray]:...
    @reprojection_errors.setter
    def reprojection_errors(self, arg1: Dict[str, numpy.ndarray]) -> None:...
class LandmarkView:
    def __contains__(self, arg0: str) -> bool: ...
    def __getitem__(self, arg0: str) -> Landmark: ...
    def __init__(self, arg0: Map) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def get(self, arg0: str) -> Landmark: ...
    def items(self) -> Iterator: ...
    def keys(self) -> Iterator: ...
    def values(self) -> Iterator: ...
class Map:
    def __init__(self) -> None: ...
    @overload
    def add_observation(self, shot: Shot, landmark: Landmark, observation: Observation) -> None: ...
    @overload
    def add_observation(self, shot_Id: str, landmark_id: str, observation: Observation) -> None: ...
    def clean_landmarks_below_min_observations(self, arg0: int) -> None: ...
    def clear_observations_and_landmarks(self) -> None: ...
    def compute_reprojection_errors(self, arg0: TracksManager, arg1: ErrorType) -> Dict[str, Dict[str, numpy.ndarray]]: ...
    def create_camera(self, camera: opensfm.pygeometry.Camera) -> opensfm.pygeometry.Camera: ...
    def create_landmark(self, lm_id: str, global_position: numpy.ndarray) -> Landmark: ...
    def create_pano_shot(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: opensfm.pygeometry.Pose) -> Shot: ...
    def create_rig_camera(self, arg0: RigCamera) -> RigCamera: ...
    def create_rig_instance(self, arg0: str) -> RigInstance: ...
    @overload
    def create_shot(self, arg0: str, arg1: str, arg2: str, arg3: str) -> Shot: ...
    @overload
    def create_shot(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: opensfm.pygeometry.Pose) -> Shot: ...
    def get_bias(self, arg0: str) -> opensfm.pygeometry.Similarity: ...
    def get_biases(self) -> BiasView: ...
    def get_camera(self, arg0: str) -> opensfm.pygeometry.Camera: ...
    def get_camera_view(self) -> CameraView: ...
    def get_cameras(self) -> CameraView: ...
    def get_landmark(self, arg0: str) -> Landmark: ...
    def get_landmark_view(self) -> LandmarkView: ...
    def get_landmarks(self) -> LandmarkView: ...
    def get_pano_shot(self, arg0: str) -> Shot: ...
    def get_pano_shots(self) -> PanoShotView: ...
    def get_reference(self) -> opensfm.pygeo.TopocentricConverter: ...
    def get_shot(self, arg0: str) -> Shot: ...
    def get_shots(self) -> ShotView: ...
    def get_valid_observations(self, arg0: TracksManager) -> Dict[str, Dict[str, Observation]]: ...
    def has_landmark(self, arg0: str) -> bool: ...
    @overload
    def remove_landmark(self, arg0: Landmark) -> None: ...
    @overload
    def remove_landmark(self, arg0: str) -> None: ...
    def remove_observation(self, shot: str, landmark: str) -> None: ...
    def remove_pano_shot(self, arg0: str) -> None: ...
    def remove_rig_instance(self, arg0: str) -> None: ...
    def remove_shot(self, arg0: str) -> None: ...
    def set_bias(self, arg0: str, arg1: opensfm.pygeometry.Similarity) -> None: ...
    def set_reference(self, arg0: float, arg1: float, arg2: float) -> None: ...
    def to_tracks_manager(self) -> TracksManager: ...
    def update_pano_shot(self, arg0: Shot) -> Shot: ...
    def update_rig_instance(self, arg0: RigInstance) -> RigInstance: ...
    def update_shot(self, arg0: Shot) -> Shot: ...
class Observation:
    def __init__(self, x: float, y: float, s: float, r: int, g: int, b: int, feature: int, segmentation: int = -1, instance: int = -1) -> None: ...
    def copy(self) -> Observation: ...
    @property
    def color(self) -> numpy.ndarray:...
    @color.setter
    def color(self, arg0: numpy.ndarray) -> None:...
    @property
    def id(self) -> int:...
    @id.setter
    def id(self, arg0: int) -> None:...
    @property
    def instance(self) -> int:...
    @instance.setter
    def instance(self, arg0: int) -> None:...
    @property
    def point(self) -> numpy.ndarray:...
    @point.setter
    def point(self, arg0: numpy.ndarray) -> None:...
    @property
    def scale(self) -> float:...
    @scale.setter
    def scale(self, arg0: float) -> None:...
    @property
    def segmentation(self) -> int:...
    @segmentation.setter
    def segmentation(self, arg0: int) -> None:...
    NO_SEMANTIC_VALUE = -1
class PanoShotView:
    def __contains__(self, arg0: str) -> bool: ...
    def __getitem__(self, arg0: str) -> Shot: ...
    def __init__(self, arg0: Map) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def get(self, arg0: str) -> Shot: ...
    def items(self) -> Iterator: ...
    def keys(self) -> Iterator: ...
    def values(self) -> Iterator: ...
class RigCamera:
    def __getstate__(self) -> tuple: ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: opensfm.pygeometry.Pose, arg1: str) -> None: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    @property
    def id(self) -> str:...
    @id.setter
    def id(self, arg0: str) -> None:...
    @property
    def pose(self) -> opensfm.pygeometry.Pose:...
    @pose.setter
    def pose(self, arg0: opensfm.pygeometry.Pose) -> None:...
class RigCameraView:
    def __contains__(self, arg0: str) -> bool: ...
    def __getitem__(self, arg0: str) -> RigCamera: ...
    def __init__(self, arg0: Map) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def get(self, arg0: str) -> RigCamera: ...
    def items(self) -> Iterator: ...
    def keys(self) -> Iterator: ...
    def values(self) -> Iterator: ...
class RigInstance:
    def __init__(self, arg0: str) -> None: ...
    def add_shot(self, arg0: RigCamera, arg1: Shot) -> None: ...
    def keys(self) -> Set[str]: ...
    def remove_shot(self, arg0: str) -> None: ...
    def update_instance_pose_with_shot(self, arg0: str, arg1: opensfm.pygeometry.Pose) -> None: ...
    def update_rig_camera_pose(self, arg0: str, arg1: opensfm.pygeometry.Pose) -> None: ...
    @property
    def camera_ids(self) -> Dict[str, str]:...
    @property
    def id(self) -> str:...
    @id.setter
    def id(self, arg0: str) -> None:...
    @property
    def pose(self) -> opensfm.pygeometry.Pose:...
    @pose.setter
    def pose(self, arg1: opensfm.pygeometry.Pose) -> None:...
    @property
    def rig_camera_ids(self) -> Dict[str, str]:...
    @property
    def rig_cameras(self) -> Dict[str, RigCamera]:...
    @property
    def shots(self) -> Dict[str, Shot]:...
class RigInstanceView:
    def __contains__(self, arg0: str) -> bool: ...
    def __getitem__(self, arg0: str) -> RigInstance: ...
    def __init__(self, arg0: Map) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def get(self, arg0: str) -> RigInstance: ...
    def items(self) -> Iterator: ...
    def keys(self) -> Iterator: ...
    def values(self) -> Iterator: ...
class Shot:
    def __init__(self, arg0: str, arg1: opensfm.pygeometry.Camera, arg2: opensfm.pygeometry.Pose) -> None: ...
    def bearing(self, arg0: numpy.ndarray) -> numpy.ndarray: ...
    def bearing_many(self, arg0: numpy.ndarray) -> numpy.ndarray: ...
    def get_landmark_observation(self, arg0: Landmark) -> Observation: ...
    def get_observation(self, arg0: int) -> Observation: ...
    def get_observation_landmark(self, arg0: int) -> Landmark: ...
    def get_valid_landmarks(self) -> List[Landmark]: ...
    def project(self, arg0: numpy.ndarray) -> numpy.ndarray: ...
    def project_many(self, arg0: numpy.ndarray) -> numpy.ndarray: ...
    def remove_observation(self, arg0: int) -> None: ...
    def set_rig(self, arg0: RigInstance, arg1: RigCamera) -> None: ...
    @property
    def camera(self) -> opensfm.pygeometry.Camera:...
    @property
    def covariance(self) -> numpy.ndarray:...
    @covariance.setter
    def covariance(self, arg1: numpy.ndarray) -> None:...
    @property
    def id(self) -> str:...
    @property
    def merge_cc(self) -> int:...
    @merge_cc.setter
    def merge_cc(self, arg0: int) -> None:...
    @property
    def mesh(self) -> ShotMesh:...
    @mesh.setter
    def mesh(self, arg0: ShotMesh) -> None:...
    @property
    def metadata(self) -> ShotMeasurements:...
    @metadata.setter
    def metadata(self, arg1: ShotMeasurements) -> None:...
    @property
    def pose(self) -> opensfm.pygeometry.Pose:...
    @pose.setter
    def pose(self, arg1: opensfm.pygeometry.Pose) -> None:...
    @property
    def rig_camera(self) -> RigCamera:...
    @property
    def rig_camera_id(self) -> str:...
    @property
    def rig_instance(self) -> RigInstance:...
    @property
    def rig_instance_id(self) -> str:...
    @property
    def scale(self) -> float:...
    @scale.setter
    def scale(self, arg0: float) -> None:...
class ShotMeasurementDouble:
    def __getstate__(self) -> tuple: ...
    def __init__(self) -> None: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def reset(self) -> None: ...
    @property
    def has_value(self) -> bool:...
    @property
    def value(self) -> float:...
    @value.setter
    def value(self, arg1: float) -> None:...
class ShotMeasurementInt:
    def __getstate__(self) -> tuple: ...
    def __init__(self) -> None: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def reset(self) -> None: ...
    @property
    def has_value(self) -> bool:...
    @property
    def value(self) -> int:...
    @value.setter
    def value(self, arg1: int) -> None:...
class ShotMeasurementString:
    def __getstate__(self) -> tuple: ...
    def __init__(self) -> None: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def reset(self) -> None: ...
    @property
    def has_value(self) -> bool:...
    @property
    def value(self) -> str:...
    @value.setter
    def value(self, arg1: str) -> None:...
class ShotMeasurementVec3d:
    def __getstate__(self) -> tuple: ...
    def __init__(self) -> None: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def reset(self) -> None: ...
    @property
    def has_value(self) -> bool:...
    @property
    def value(self) -> numpy.ndarray:...
    @value.setter
    def value(self, arg1: numpy.ndarray) -> None:...
class ShotMeasurements:
    def __copy__(self) -> ShotMeasurements: ...
    def __getstate__(self) -> tuple: ...
    def __init__(self) -> None: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def set(self, arg0: ShotMeasurements) -> None: ...
    @property
    def accelerometer(self) -> ShotMeasurementVec3d:...
    @accelerometer.setter
    def accelerometer(self, arg0: ShotMeasurementVec3d) -> None:...
    @property
    def attributes(self) -> Dict[str, str]:...
    @attributes.setter
    def attributes(self, arg1: Dict[str, str]) -> None:...
    @property
    def capture_time(self) -> ShotMeasurementDouble:...
    @capture_time.setter
    def capture_time(self, arg0: ShotMeasurementDouble) -> None:...
    @property
    def compass_accuracy(self) -> ShotMeasurementDouble:...
    @compass_accuracy.setter
    def compass_accuracy(self, arg0: ShotMeasurementDouble) -> None:...
    @property
    def compass_angle(self) -> ShotMeasurementDouble:...
    @compass_angle.setter
    def compass_angle(self, arg0: ShotMeasurementDouble) -> None:...
    @property
    def gps_accuracy(self) -> ShotMeasurementDouble:...
    @gps_accuracy.setter
    def gps_accuracy(self, arg0: ShotMeasurementDouble) -> None:...
    @property
    def gps_position(self) -> ShotMeasurementVec3d:...
    @gps_position.setter
    def gps_position(self, arg0: ShotMeasurementVec3d) -> None:...
    @property
    def opk_accuracy(self) -> ShotMeasurementDouble:...
    @opk_accuracy.setter
    def opk_accuracy(self, arg0: ShotMeasurementDouble) -> None:...
    @property
    def opk_angles(self) -> ShotMeasurementVec3d:...
    @opk_angles.setter
    def opk_angles(self, arg0: ShotMeasurementVec3d) -> None:...
    @property
    def orientation(self) -> ShotMeasurementInt:...
    @orientation.setter
    def orientation(self, arg0: ShotMeasurementInt) -> None:...
    @property
    def sequence_key(self) -> ShotMeasurementString:...
    @sequence_key.setter
    def sequence_key(self, arg0: ShotMeasurementString) -> None:...
class ShotMesh:
    @property
    def faces(self) -> numpy.ndarray:...
    @faces.setter
    def faces(self, arg1: numpy.ndarray) -> None:...
    @property
    def vertices(self) -> numpy.ndarray:...
    @vertices.setter
    def vertices(self, arg1: numpy.ndarray) -> None:...
class ShotView:
    def __contains__(self, arg0: str) -> bool: ...
    def __getitem__(self, arg0: str) -> Shot: ...
    def __init__(self, arg0: Map) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def get(self, arg0: str) -> Shot: ...
    def items(self) -> Iterator: ...
    def keys(self) -> Iterator: ...
    def values(self) -> Iterator: ...
class TracksManager:
    def __init__(self) -> None: ...
    def add_observation(self, arg0: str, arg1: str, arg2: Observation) -> None: ...
    def as_string(self) -> str: ...
    def construct_sub_tracks_manager(self, arg0: List[str], arg1: List[str]) -> TracksManager: ...
    def get_all_common_observations(self, arg0: str, arg1: str) -> List[Tuple[str, Observation, Observation]]: ...
    def get_all_pairs_connectivity(self, shots: List[str] = [], tracks: List[str] = []) -> Dict[Tuple[str, str], int]: ...
    def get_observation(self, arg0: str, arg1: str) -> Observation: ...
    def get_shot_ids(self) -> List[str]: ...
    def get_shot_observations(self, arg0: str) -> Dict[str, Observation]: ...
    def get_track_ids(self) -> List[str]: ...
    def get_track_observations(self, arg0: str) -> Dict[str, Observation]: ...
    @staticmethod
    def instanciate_from_file(arg0: str) -> TracksManager: ...
    @staticmethod
    def instanciate_from_string(arg0: str) -> TracksManager: ...
    @staticmethod
    def merge_tracks_manager(arg0: List[TracksManager]) -> TracksManager: ...
    def num_shots(self) -> int: ...
    def num_tracks(self) -> int: ...
    def remove_observation(self, arg0: str, arg1: str) -> None: ...
    def write_to_file(self, arg0: str) -> None: ...
Angular = ...
Normalized = ...
Pixel = ...