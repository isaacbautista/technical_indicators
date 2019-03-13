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
test = np.array([25, 24.875, 24.781, 24.594, 24.50, 24.625, 25.219, 27.25])

sma = sma(test, 5)

for x in sma:
    print(x)
```

### EMA

```python
test = np.array([25, 24.875, 24.781, 24.594, 24.5, 24.625, 25.219, 27.25])

ema = ema(test, 10)

for x in ema:
    print(x)
```

### Bollinger Bands

```python
test = np.array([31.875, 32.125, 32.3125, 32.125, 31.875, 32.3125, 32.25,
                     32.4375, 32.8125, 32.375, 32.5, 32.4375, 32.75, 33.1875,
                     33.0625, 33.0625, 33.125, 33.0625, 32.8125, 32.875, 33.25,
                     33.125])

lower, middle, upper = bollinger_bands(test, window=5)

for i in range(len(lower)):
    print("{:.4f}\t{:.4f}\t{:.4f}".format(middle[i], upper[i], lower[i]))
```
