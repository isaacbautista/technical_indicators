# A technical indicators library written in Python3

## General

The following indicators are available:

Standard Moving Average (SMA)
Exponential Moving Average (EMA)
Bollinger Bands
Wilder Smoothing
Relative Strength Index (RSI)
Moving Average Convergence/Divergence (MACD)
Stochastic
Stochastic RSI
Momentum

## Usage

### SMA

```python
# list of prices to test

test = np.array([25, 24.875, 24.781, 24.594, 24.5, 24.625, 25.219, 27.25])

ema = ema(test, 10)

for x in ema:
    print(x)
```
