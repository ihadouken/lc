int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration){
    int cooldown, ptime, i;
    ptime = 0;

    for (i = 1; i < timeSeriesSize; i++) {
        /* Find relative time of current attack with previous. */
        cooldown = timeSeries[i] - timeSeries[i-1];

        /* Ashe attacked after cooldown, suffers all of poison peroid. */
        if (cooldown > duration - 1)
            ptime += duration;
        /* Ashe attacked while poisoned, poison period ends prematurely. */
        else
            ptime += cooldown;
    }

    /* Last poison period has to be suffered unconditionally. */
    ptime += duration;
    return ptime;
}
