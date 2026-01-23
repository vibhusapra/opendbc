from opendbc.car import structs, get_safety_config
from opendbc.car.interfaces import CarInterfaceBase
from opendbc.car.volvo.carcontroller import CarController
from opendbc.car.volvo.carstate import CarState

TransmissionType = structs.CarParams.TransmissionType


class CarInterface(CarInterfaceBase):
  CarState = CarState
  CarController = CarController

  @staticmethod
  def _get_params(ret: structs.CarParams, candidate, fingerprint, car_fw, alpha_long, is_release, docs) -> structs.CarParams:
    ret.brand = 'volvo'

    # Volvo safety model not implemented in panda firmware yet
    # Using noOutput for dashcam mode (no steering control)
    ret.safetyConfigs = [get_safety_config(structs.CarParams.SafetyModel.noOutput)]
    # TODO: Implement volvo safety in panda/board/safety/
    #ret.safetyConfigs = [get_safety_config(structs.CarParams.SafetyModel.volvo)]

    ret.dashcamOnly = True  # Dashcam mode until volvo safety is implemented

    ret.steerActuatorDelay = 0.3
    ret.steerLimitTimer = 0.1
    ret.steerAtStandstill = True

    # Use angle-based steering control for Volvo CMA platform
    ret.steerControlType = structs.CarParams.SteerControlType.angle
    # Note: No lateral tuning configuration needed for basic angle control
    ret.radarUnavailable = True

    ret.alphaLongitudinalAvailable = False

    ret.pcmCruise = True

    return ret