import numpy as np

class TA:
    ########## TECHNICAL INDICATORS ##########

    def sma(self, data, window):
        """
        sma - standard moving average
        data   (list)
        window (int)

        returns np.array
        """

        # exception handling, taking out nans
        nan_count = 0
        for element in data:
            if np.isnan(element):
                data = np.delete(data, 0)
                nan_count += 1

        sma = np.array([])
        for i in range(window-1):
            sma = np.append(sma, np.nan)

        for i in range(0, len(data) - window + 1):
            sma = np.append(sma, np.mean(data[i:i+window]))

        # exception handling, adding back the nans
        for i in range(nan_count):
            data = np.insert(data, 0, np.nan)
            sma = np.insert(sma, 0, np.nan)


        return sma

    def ema(self, data, window):
        """
        ema - exponential moving average
        data   (list)
        window (int)

        returns np.array
        """

        # exception handling, taking out nans
        nan_count = 0
        for element in data:
            if np.isnan(element):
                data = np.delete(data, 0)
                nan_count += 1

        # multiplier = (2/(window + 1))
        # ema = (closing price - EMA(previous))*multiplier + EMA(previous)

        ema = np.array([])
        multiplier = 2 / (window + 1)
        ema = np.append(ema, data[0])

        for i in range(1, len(data)):
            new = data[i]*multiplier + ema[i-1]*(1 - multiplier)
            ema = np.append(ema, new)

        # exception handling, adding back the nans
        for i in range(nan_count):
            data = np.insert(data, 0, np.nan)
            ema = np.insert(ema, 0, np.nan)

        return ema

    def ema_percent(self, data, percent):
        """
        ema - exponential moving average

        data    (list)
        percent (int)

        returns np.array
        """


        # exception handling, taking out nans
        nan_count = 0
        for element in data:
            if np.isnan(element):
                data = np.delete(data, 0)
                nan_count += 1

        ema = np.array([])
        multiplier = percent
        ema = np.append(ema, data[0])

        for i in range(1, len(data)):
            new = data[i]*multiplier + ema[i-1]*(1 - multiplier)
            ema = np.append(ema, new)

        # exception handling, adding back the nans
        for i in range(nan_count):
            data = np.insert(data, 0, np.nan)
            ema = np.insert(ema, 0, np.nan)

        return ema

    def bollinger_bands(self, data, window=20):
        """
        bollinger bands
        data   (list)
        window (int)

        returns lower_band (np.array), middle_band (np.array), upper_band (np.array)
        """

        # exception handling, taking out nans
        nan_count = 0
        for element in data:
            if np.isnan(element):
                data = np.delete(data, 0)
                nan_count += 1

        middle_band = self.sma(data, window)

        close_std = np.array([])

        for i in range(window-1):
            close_std = np.append(close_std, np.nan)

        for i in range(0, len(data) - window + 1):
            close_std = np.append(close_std, 2 * np.std(data[i:i+window]))

        lower_band = middle_band - close_std
        upper_band = middle_band + close_std

        # exception handling, adding back the nans
        for i in range(nan_count):
            data = np.insert(data, 0, np.nan)
            lower_band = np.insert(lower_band, 0, np.nan)
            middle_band = np.insert(middle_band, 0, np.nan)
            upper_band = np.insert(upper_band, 0, np.nan)

        return lower_band, middle_band, upper_band

    def wilder_smooth(self, data, window=14):
        """
        wilder_smooth - previous MA + (1/n)(close - previous MA)

        data   (list)
        window (int)

        returns np.array
        """

        # exception handling, taking out nans
        nan_count = 0
        for element in data:
            if np.isnan(element):
                data = np.delete(data, 0)
                nan_count += 1

        previous_ma = self.sma(data, window)

        wilder = np.array([])

        for i in range(window-1):
            wilder = np.append(wilder, np.nan)


        wilder = np.append(wilder, previous_ma[window-1])

        for i in range(window, len(data)):
            sum = wilder[i-1] + (1/window)*(data[i] - wilder[i-1])
            wilder = np.append(wilder, sum)

        # exception handling, adding back the nans
        for i in range(nan_count):
            data = np.insert(data, 0, np.nan)
            wilder = np.insert(wilder, 0, np.nan)

        return wilder

    def rsi(self, data, window=14):
        """
        rsi - relative strength index

        data   (list)
        window (int)

        returns np.array
        """

        # rsi = 100 - (100 / (1 + U/D) )
        # U = avg of upward price change
        # D = avg of downward price change

        # exception handling, taking out nans
        nan_count = 0
        for element in data:
            if np.isnan(element):
                data = np.delete(data, 0)
                nan_count += 1

        #
        # find upward/downward price change for every day
        #
        upward_change = np.array([np.nan])
        downward_change = np.array([np.nan])

        for i in range(len(data)-1):
            change = data[i+1] - data[i]
            if change > 0:
                upward_change = np.append(upward_change, change)
                downward_change = np.append(downward_change, 0)

            if change < 0:
                upward_change = np.append(upward_change, 0)
                downward_change = np.append(downward_change, np.abs(change))

            if change == 0:
                upward_change = np.append(upward_change, 0)
                downward_change = np.append(downward_change, 0)

        #
        # apply Wilder's Smoothing to upward/downward change
        #

        upward_smooth = self.wilder_smooth(upward_change[1:], window)
        downward_smooth = self.wilder_smooth(downward_change[1:], window)

        #
        # need to prepend a nan to make verything work
        #

        upward_smooth = np.insert(upward_smooth, 0, np.nan)
        downward_smooth = np.insert(downward_smooth, 0, np.nan)

        #
        # compute rsi
        #

        rsi = 100 - (100 / (1 + upward_smooth/downward_smooth))

        # exception handling, adding back the nans
        for i in range(nan_count):
            data = np.insert(data, 0, np.nan)
            rsi = np.insert(rsi, 0, np.nan)

        return rsi

    def macd(self, data, fastperiod=12, slowperiod=26, signalperiod=9):
        """
        macd - Moving Average Convergence/Divergence

        data         (list)
        fastperiod   (int)
        slowperiod   (int)
        signalperiod (int)

        returns macd (np.array), macd_signal (np.array)
        """

        # exception handling, taking out nans
        nan_count = 0
        for element in data:
            if np.isnan(element):
                data = np.delete(data, 0)
                nan_count += 1

        fast_ema = self.ema_percent(data, 0.150)
        slow_ema = self.ema_percent(data, 0.075)

        macd = np.array([])

        for i in range(slowperiod -1, len(fast_ema)):
            macd = np.append(macd, fast_ema[i] - slow_ema[i])

        macd_signal = self.ema_percent(macd, 0.200)

        for i in range(slowperiod - 1):
            macd = np.insert(macd, 0, np.nan)

        for i in range(slowperiod - 1):
            macd_signal = np.insert(macd_signal, 0, np.nan)

        # exception handling, adding back the nans
        for i in range(nan_count):
            data = np.insert(data, 0, np.nan)
            macd = np.insert(macd, 0, np.nan)
            macd_signal = np.insert(macd_signal, 0, np.nan)

        return macd, macd_signal

    def stochastic(self, high, low, close, k_periods=14, k_slow_periods=3, d_periods=3):
        """
            high  (list)
            low   (list)
            close (list)

            k_periods: (int)
            # of periods used in the stochastic calculation

            k_slow_periods: (int)
            controls internal smoothing of k.
            1 is considered a fast stochastic, 3 is a slow stochastic

            d_periods: (int)
            # of periods used to calculate the sma of k

            returns k (np.array), d (np.array)
        """
        # stoch oscillator is two lines
        # main line is k (usually a solid line)
        # second line, d, is a moving average of k (usually a dotted line)


        # formula for k
        # 100 * (close - lowest low in k periods) / (highest high in k periods - lowest low in k periods)

        # find the highest high and lowest low in last k_periods
        highs = np.array([])
        lows  = np.array([])

        for i in range(0, len(high) - k_periods + 1):
            highs = np.append(highs, np.max(high[i:i+k_periods]))
            lows = np.append(lows, np.min(low[i:i+k_periods]))

        # use formula for k, apply smoothing

        x = close[k_periods-1:] - lows
        y = highs - lows

        sum_x = np.array([])
        sum_y = np.array([])

        for i in range(0, len(x) - k_slow_periods + 1):
            sum_x = np.append(sum_x, np.sum(x[i:i+k_slow_periods]))
            sum_y = np.append(sum_y, np.sum(y[i:i+k_slow_periods]))

        k = 100 * (sum_x / sum_y)

        # calculate d, which is an sma of k

        d = self.sma(k, d_periods)

        # fix the formatting of our arrays
        for i in range(k_periods - 1):
            lows = np.insert(lows, 0, np.nan)
            highs = np.insert(highs, 0, np.nan)
            x = np.insert(x, 0, np.nan)
            y = np.insert(y, 0, np.nan)

        for i in range(k_periods - 1 + k_slow_periods -1):
            sum_x = np.insert(sum_x, 0, np.nan)
            sum_y = np.insert(sum_y, 0, np.nan)
            k = np.insert(k, 0, np.nan)
            d = np.insert(d, 0, np.nan)

        # # exception handling, adding back the nans
        # for i in range(nan_count):
        #     data = np.insert(data, 0, np.nan)
        #     k = np.insert(data, 0, np.nan)
        #     d = np.insert(data, 0, np.nan)

        return k, d

    def stoch_rsi(self, close, rsi_length=14, k_periods=14, k_slow_periods=3, d_periods=3):

        """
            close (list)

            rsi_length     (int)
            k_periods      (int)
            k_slow_periods (int)
            d_periods      (int)

            returns k (np.array), d (np.array)
        """

        # compute rsi
        rsi = self.rsi(close, window=rsi_length)

        # remove nan's from the front of rsi, we'll add them back later
        for element in rsi:
            if np.isnan(element):
                rsi = np.delete(rsi, 0)

        # compute stochastic
        # find the high/low rsi in last k_periods
        highs = np.array([])
        lows  = np.array([])

        for i in range(0, len(rsi) - k_periods + 1):
            highs = np.append(highs, np.max(rsi[i:i+k_periods]))
            lows = np.append(lows, np.min(rsi[i:i+k_periods]))

        # print(len(rsi[k_periods-1:]), len(highs), len(lows), len(close))

        # use formula for k, apply smoothing
        x = rsi[k_periods-1:] - lows
        y = highs - lows

        sum_x = np.array([])
        sum_y = np.array([])

        for i in range(0, len(x) - k_slow_periods + 1):
            sum_x = np.append(sum_x, np.sum(x[i:i+k_slow_periods]))
            sum_y = np.append(sum_y, np.sum(y[i:i+k_slow_periods]))

        k = 100 * (sum_x / sum_y)

        # calculate d, which is an sma of k

        d = self.sma(k, d_periods)

        # fix the formatting of our arrays
        for i in range(rsi_length):
            rsi = np.insert(rsi, 0, np.nan)

        for i in range(k_periods - 1 + rsi_length):
            lows = np.insert(lows, 0, np.nan)
            highs = np.insert(highs, 0, np.nan)
            x = np.insert(x, 0, np.nan)
            y = np.insert(y, 0, np.nan)

        for i in range(k_periods - 1 + k_slow_periods -1 + rsi_length):
            sum_x = np.insert(sum_x, 0, np.nan)
            sum_y = np.insert(sum_y, 0, np.nan)
            k = np.insert(k, 0, np.nan)
            d = np.insert(d, 0, np.nan)

        return k, d

    def momentum(self, close, n=10):
        """
        momentum

        close (list)
        n     (int)

        returns np.array
        """

        # exception handling, taking out nans
        nan_count = 0
        for element in close:
            if np.isnan(element):
                data = np.delete(data, 0)
                nan_count += 1

        # calculate price n days ago
        momentum = np.array([])

        for i in range(n):
            momentum = np.insert(momentum, 0, np.nan)

        for i in range(n, len(close)):
            # momentum = np.append(momentum, 100*(close[i] / close[i-n]))0
            momentum = np.append(momentum, close[i] - close[i-n])

        # exception handling, adding back the nans
        for i in range(nan_count):
            close = np.insert(close, 0, np.nan)
            momentum = np.insert(momentum, 0, np.nan)

        return momentum
