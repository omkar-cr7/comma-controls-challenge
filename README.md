# comma-controls-challenge

My submission for the comma.ai Controls Challenge.

## Results

| Controller        | LatAccel Cost | Jerk Cost | Total Cost |
| ----------------- | ------------- | --------- | ---------- |
| Baseline PID      | 1.695         | 25.490    | 110.255    |
| Custom Controller | 1.537         | 20.246    | 97.096     |

## Approach

The baseline controller uses a simple PID loop based on lateral acceleration error.

My controller extends the baseline with:

* Feedforward control using target lateral acceleration
* Preview control using future trajectory information from `future_plan`
* Integral windup protection through clipping
* Action smoothing / rate limiting to reduce jerk

The primary goal was to improve trajectory tracking while reducing jerk and maintaining stability across the full evaluation dataset.

## Evaluation

The controller was evaluated on the full 5000-segment dataset provided in the challenge repository.

Result:

* Baseline PID Total Cost: **110.255**
* Custom Controller Total Cost: **97.096**

This represents approximately a **12% improvement** over the baseline controller.
