from . import BaseController
import numpy as np


class Controller(BaseController):
  def __init__(self):
    self.p = 0.20
    self.i = 0.085
    self.d = -0.060
    self.ff = 0.08
    self.preview = 0.10

    self.error_integral = 0.0
    self.prev_error = 0.0
    self.prev_action = 0.0

  def update(self, target_lataccel, current_lataccel, state, future_plan):
    error = target_lataccel - current_lataccel

    self.error_integral += error
    self.error_integral = float(np.clip(self.error_integral, -12.0, 12.0))

    error_diff = error - self.prev_error
    self.prev_error = error

    future_term = 0.0
    try:
      la = np.asarray(future_plan.lataccel)
      if len(la) > 10:
        future_term = float(0.6 * la[3] + 0.4 * la[8] - target_lataccel)
    except Exception:
      future_term = 0.0

    raw_action = (
      self.p * error
      + self.i * self.error_integral
      + self.d * error_diff
      + self.ff * target_lataccel
      + self.preview * future_term
    )

    max_delta = 0.18
    action = float(np.clip(raw_action, self.prev_action - max_delta, self.prev_action + max_delta))

    self.prev_action = action
    return action
