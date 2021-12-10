import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# process_file() takes a string with a path to the .csv


def process_file(pathname):
    res = pd.read_csv(pathname, sep=',', header=0, index_col=None, names=[
                      'time', 'seconds', 'z', 'y', 'x'])
    return res


def read_dlp_data():
    # Left pocket
    dlp_5min = process_file('data/5minlp.csv')
    dlp_5min = dlp_5min[(dlp_5min['seconds'] >= 30) &
                        (dlp_5min['seconds'] <= 330)]
    dlp_5min['seconds'] = dlp_5min['seconds'] - 30
    dlp_5min = dlp_5min.iloc[0:14000, :]
    return dlp_5min


def read_drp_data():
    # Right pocket
    drp_5min = process_file('data/5minrp.csv')
    drp_5min = drp_5min[(drp_5min['seconds'] >= 30) &
                        (drp_5min['seconds'] <= 330)]
    drp_5min['seconds'] = drp_5min['seconds'] - 30
    drp_5min = drp_5min.iloc[0:14000, :]
    return drp_5min

# 5 minutes waking data- Matt


def read_mrp_data():
    # Right pocket
    mrp_5min = process_file('data/matt_rp50_5mins_screeon.csv')
    mrp_5min = mrp_5min[(mrp_5min['seconds'] >= 10) &
                        (mrp_5min['seconds'] <= 310)]
    mrp_5min['seconds'] = mrp_5min['seconds'] - 10
    mrp_5min = mrp_5min.iloc[0:14000, :]
    return mrp_5min

# 5 minutes waking data- Sidak


def read_srp_data():
    # Right pocket
    srp_5min = process_file('data/sam_rp50_5mins.csv')
    srp_5min = srp_5min[(srp_5min['seconds'] >= 30) &
                        (srp_5min['seconds'] <= 330)]
    srp_5min['seconds'] = srp_5min['seconds'] - 30
    srp_5min = srp_5min.iloc[0:14000, :]
    return srp_5min


def read_slp_data():
    # Left pocket
    slp_5min = process_file('data/sam_lp50_5mins.csv')
    slp_5min = slp_5min[(slp_5min['seconds'] >= 30) &
                        (slp_5min['seconds'] <= 330)]
    slp_5min['seconds'] = slp_5min['seconds'] - 30
    slp_5min = slp_5min.iloc[0:14000, :]
    return slp_5min


def read_mrp_upstairs_long_data():
    mrp_upstairs_long = process_file('data/matt_upstairs_long.csv')
    mrp_upstairs_long = mrp_upstairs_long[(
        mrp_upstairs_long['seconds'] > 6) & (mrp_upstairs_long['seconds'] < 53)]
    mrp_upstairs_long['seconds'] = mrp_upstairs_long['seconds'] - 6
    return mrp_upstairs_long


def read_mrp_downstairs_long_data():
    mrp_downstairs_long = process_file('data/matt_upstairs_long.csv')
    mrp_downstairs_long = mrp_downstairs_long[(
        mrp_downstairs_long['seconds'] > 6) & (mrp_downstairs_long['seconds'] < 53)]
    mrp_downstairs_long['seconds'] = mrp_downstairs_long['seconds'] - 6
    return mrp_downstairs_long


def read_mrp_upstairs_16steps_data():
    mrp_upstairs_16steps = process_file('data/matt_upstairs_16stpes.csv')
    mrp_upstairs_16steps = mrp_upstairs_16steps[(
        mrp_upstairs_16steps['seconds'] > 8) & (mrp_upstairs_16steps['seconds'] < 20)]
    mrp_upstairs_16steps['seconds'] = mrp_upstairs_16steps['seconds'] - 8
    return mrp_upstairs_16steps


def read_mrp_downstairs_16steps_data():
    mrp_downstairs_16steps = process_file('data/matt_downstairs_16steps.csv')
    mrp_downstairs_16steps = mrp_downstairs_16steps[(
        mrp_downstairs_16steps['seconds'] > 10) & (mrp_downstairs_16steps['seconds'] < 20)]
    mrp_downstairs_16steps['seconds'] = mrp_downstairs_16steps['seconds'] - 10
    return mrp_downstairs_16steps


def read_mrp_smallrun_data():
    mrp_smallrun = process_file('data/matt_small_run2.csv')
    mrp_smallrun = mrp_smallrun[(
        mrp_smallrun['seconds'] > 5) & (mrp_smallrun['seconds'] < 45)]
    mrp_smallrun['seconds'] = mrp_smallrun['seconds'] - 5
    return mrp_smallrun


def read_mrp_smallrun_2_data():
    mrp_smallrun_2 = process_file('data/matt_small_run2.csv')
    mrp_smallrun_2 = mrp_smallrun_2[(
        mrp_smallrun_2['seconds'] > 5) & (mrp_smallrun_2['seconds'] < 45)]
    mrp_smallrun_2['seconds'] = mrp_smallrun_2['seconds'] - 5
    return mrp_smallrun_2


def read_mrp_fastrun_data():
    mrp_fastrun = process_file('data/matt_fast_run.csv')
    mrp_fastrun = mrp_fastrun[(
        mrp_fastrun['seconds'] > 3) & (mrp_fastrun['seconds'] < 25)]
    mrp_fastrun['seconds'] = mrp_fastrun['seconds'] - 3
    return mrp_fastrun


def read_m_up24_1_data():
    m_up24_1 = process_file('data/matt_upstairs_24steps_1.csv')
    m_up24_1 = m_up24_1[(m_up24_1['seconds'] > 6.5) & (
        m_up24_1['seconds'] < 22)]
    m_up24_1['seconds'] = m_up24_1['seconds'] - 6.5
    return m_up24_1


def read_m_up24_2_data():
    m_up24_2 = process_file('data/matt_upstairs_24steps_2.csv')
    m_up24_2 = m_up24_2[(m_up24_2['seconds'] > 5) & (
        m_up24_2['seconds'] < 20.5)]
    m_up24_2['seconds'] = m_up24_2['seconds'] - 5
    return m_up24_2


def read_m_up24_3_data():
    m_up24_3 = process_file('data/matt_upstairs_24steps_3.csv')
    m_up24_3 = m_up24_3[(m_up24_3['seconds'] > 4) & (
        m_up24_3['seconds'] < 20.5)]
    m_up24_3['seconds'] = m_up24_3['seconds'] - 4
    return m_up24_3


def read_m_up24_4_data():
    m_up24_4 = process_file('data/matt_upstairs_24steps_4.csv')
    m_up24_4 = m_up24_4[(m_up24_4['seconds'] > 4) & (
        m_up24_4['seconds'] < 19.5)]
    m_up24_4['seconds'] = m_up24_4['seconds'] - 4
    return m_up24_4


def read_m_up24_5_data():
    m_up24_5 = process_file('data/matt_upstairs_24steps_5.csv')
    m_up24_5 = m_up24_5[(m_up24_5['seconds'] > 5) & (
        m_up24_5['seconds'] < 19.5)]
    m_up24_5['seconds'] = m_up24_5['seconds'] - 5
    return m_up24_5


def read_m_down24_1_data():
    m_down24_1 = process_file('data/matt_downstairs_24steps_1.csv')
    m_down24_1 = m_down24_1[(m_down24_1['seconds'] > 7) & (
        m_down24_1['seconds'] < 21.5)]
    m_down24_1['seconds'] = m_down24_1['seconds'] - 7
    return m_down24_1


def read_m_down24_2_data():
    m_down24_2 = process_file('data/matt_downstairs_24steps_2.csv')
    m_down24_2 = m_down24_2[(m_down24_2['seconds'] > 5.5) & (
        m_down24_2['seconds'] < 20)]
    m_down24_2['seconds'] = m_down24_2['seconds'] - 5.5
    return m_down24_2


def read_m_down24_3_data():
    m_down24_3 = process_file('data/matt_downstairs_24steps_3.csv')
    m_down24_3 = m_down24_3[(m_down24_3['seconds'] > 5) & (
        m_down24_3['seconds'] < 19)]
    m_down24_3['seconds'] = m_down24_3['seconds'] - 5
    return m_down24_3


def read_m_down24_4_data():
    m_down24_4 = process_file('data/matt_downstairs_24steps_4.csv')
    m_down24_4 = m_down24_4[(m_down24_4['seconds'] > 5) & (
        m_down24_4['seconds'] < 19)]
    m_down24_4['seconds'] = m_down24_4['seconds'] - 5
    return m_down24_4


def read_m_down24_5_data():
    m_down24_5 = process_file('data/matt_downstairs_24steps_5.csv')
    m_down24_5 = m_down24_5[(m_down24_5['seconds'] > 5) & (
        m_down24_5['seconds'] < 19)]
    m_down24_5['seconds'] = m_down24_5['seconds'] - 5
    return m_down24_5


def read_d_run_data():
    d_run_4min = process_file('data/drun4min.csv')
    d_run_4min = d_run_4min[(d_run_4min['seconds'] > 20) &
                            (d_run_4min['seconds'] < 230)]
    d_run_4min['seconds'] = d_run_4min['seconds'] - 20
    return d_run_4min


def read_d_up_1_data():
    d_up_1 = process_file('data/d_up1.csv')
    d_up_1 = d_up_1[(d_up_1['seconds'] > 12) & (d_up_1['seconds'] < 24)]
    d_up_1['seconds'] = d_up_1['seconds'] - 12
    return d_up_1


def read_d_up_2_data():
    d_up_2 = process_file('data/d_up2.csv')
    d_up_2 = d_up_2[(d_up_2['seconds'] > 11) & (d_up_2['seconds'] < 23)]
    d_up_2['seconds'] = d_up_2['seconds'] - 11
    return d_up_2


def read_d_up_3_data():
    d_up_3 = process_file('data/d_up3.csv')
    d_up_3 = d_up_3[(d_up_3['seconds'] > 13) & (d_up_3['seconds'] < 26)]
    d_up_3['seconds'] = d_up_3['seconds'] - 13
    return d_up_3


def read_d_up_4_data():
    d_up_4 = process_file('data/d_up4.csv')
    d_up_4 = d_up_4[(d_up_4['seconds'] > 12) & (d_up_4['seconds'] < 23)]
    d_up_4['seconds'] = d_up_4['seconds'] - 12
    return d_up_4


def read_d_down_1_data():
    d_down_1 = process_file('data/d_down1.csv')
    d_down_1 = d_down_1[(d_down_1['seconds'] > 15) &
                        (d_down_1['seconds'] < 27)]
    d_down_1['seconds'] = d_down_1['seconds'] - 15
    return d_down_1


def read_d_down_2_data():
    d_down_2 = process_file('data/d_down2.csv')
    d_down_2 = d_down_2[(d_down_2['seconds'] > 12) &
                        (d_down_2['seconds'] < 24)]
    d_down_2['seconds'] = d_down_2['seconds'] - 12
    return d_down_2


def read_d_down_3_data():
    d_down_3 = process_file('data/d_down3.csv')
    d_down_3 = d_down_3[(d_down_3['seconds'] > 8) & (d_down_3['seconds'] < 21)]
    d_down_3['seconds'] = d_down_3['seconds'] - 8
    return d_down_3


def read_d_down_4_data():
    d_down_4 = process_file('data/d_down4.csv')
    d_down_4 = d_down_4[(d_down_4['seconds'] > 11) &
                        (d_down_4['seconds'] < 22)]
    d_down_4['seconds'] = d_down_4['seconds'] - 11
    return d_down_4


def read_dlp_upstairs_1_data():
    dlp_upstairs_1 = process_file('data/dstepup1.csv')
    dlp_upstairs_1 = dlp_upstairs_1[dlp_upstairs_1['seconds'] > 12]
    dlp_upstairs_1 = dlp_upstairs_1[dlp_upstairs_1['seconds'] < 21]
    dlp_upstairs_1['seconds'] = dlp_upstairs_1['seconds'] - 12
    return dlp_upstairs_1


def read_dlp_upstairs_2_data():
    dlp_upstairs_2 = process_file('data/dstepup1.csv')
    dlp_upstairs_2 = dlp_upstairs_2[dlp_upstairs_2['seconds'] > 12]
    dlp_upstairs_2 = dlp_upstairs_2[dlp_upstairs_2['seconds'] < 21]
    dlp_upstairs_2['seconds'] = dlp_upstairs_2['seconds'] - 12
    return dlp_upstairs_2


def read_dlp_downstairs_1_data():
    dlp_downstairs_1 = process_file('data/dstepdown1.csv')
    dlp_downstairs_1 = dlp_downstairs_1[dlp_downstairs_1['seconds'] > 12]
    dlp_downstairs_1 = dlp_downstairs_1[dlp_downstairs_1['seconds'] < 21]
    dlp_downstairs_1['seconds'] = dlp_downstairs_1['seconds'] - 12
    return dlp_downstairs_1


def read_dlp_downstairs_2_data():
    dlp_downstairs_2 = process_file('data/dstepdown2.csv')
    dlp_downstairs_2 = dlp_downstairs_2[dlp_downstairs_2['seconds'] > 15.5]
    dlp_downstairs_2 = dlp_downstairs_2[dlp_downstairs_2['seconds'] < 23]
    dlp_downstairs_2['seconds'] = dlp_downstairs_2['seconds'] - 15.5
    return dlp_downstairs_2


def main():

    # read 5 mins data
    dlp_5min = read_dlp_data()
    drp_5min = read_drp_data()
    mrp_5min = read_mrp_data()
    slp_5min = read_slp_data()
    srp_5min = read_srp_data()

    # read human-activities data
    mrp_upstairs_long = read_mrp_upstairs_long_data()
    mrp_downstairs_long = read_mrp_downstairs_long_data()
    mrp_upstairs_16steps = read_mrp_upstairs_16steps_data()
    mrp_downstairs_16steps = read_mrp_downstairs_16steps_data()
    mrp_smallrun = read_mrp_smallrun_data()
    mrp_smallrun_2 = read_mrp_smallrun_2_data()
    mrp_fastrun = read_mrp_fastrun_data()

    m_up24_1 = read_m_up24_1_data()
    m_up24_2 = read_m_up24_2_data()
    m_up24_3 = read_m_up24_3_data()
    m_up24_4 = read_m_up24_4_data()
    m_up24_5 = read_m_up24_5_data()

    m_down24_1 = read_m_down24_1_data()
    m_down24_2 = read_m_down24_2_data()
    m_down24_3 = read_m_down24_3_data()
    m_down24_4 = read_m_down24_4_data()
    m_down24_5 = read_m_down24_5_data()

    d_run_4min = read_d_run_data()

    d_up_1 = read_d_up_1_data()
    d_up_2 = read_d_up_2_data()
    d_up_3 = read_d_up_3_data()
    d_up_4 = read_d_up_4_data()

    d_down_1 = read_d_down_1_data()
    d_down_2 = read_d_down_2_data()
    d_down_3 = read_d_down_3_data()
    d_down_4 = read_d_down_4_data()

    dlp_upstairs_1 = read_dlp_upstairs_1_data()
    dlp_upstairs_2 = read_dlp_upstairs_2_data()
    dlp_downstairs_1 = read_dlp_downstairs_1_data()
    dlp_downstairs_2 = read_dlp_downstairs_2_data()

    # write out 5 mins data
    dlp_5min.to_csv('processed_data/dlp_5min.csv', index=False)
    drp_5min.to_csv('processed_data/drp_5min.csv', index=False)
    mrp_5min.to_csv('processed_data/mrp_5min.csv', index=False)
    slp_5min.to_csv('processed_data/slp_5min.csv', index=False)
    srp_5min.to_csv('processed_data/srp_5min.csv', index=False)

    # write out human-activities data
    mrp_upstairs_long.to_csv(
        'processed_data/mrp_upstairs_long.csv', index=False)
    mrp_downstairs_long.to_csv(
        'processed_data/mrp_downstairs_long.csv', index=False)
    mrp_upstairs_16steps.to_csv(
        'processed_data/mrp_upstairs_16steps.csv', index=False)
    mrp_downstairs_16steps.to_csv(
        'processed_data/mrp_downstairs_16steps.csv', index=False)
    mrp_smallrun.to_csv(
        'processed_data/mrp_smallrun.csv', index=False)
    mrp_smallrun_2.to_csv(
        'processed_data/mrp_smallrun_2.csv', index=False)
    mrp_fastrun.to_csv(
        'processed_data/mrp_fastrun.csv', index=False)

    m_up24_1.to_csv(
        'processed_data/m_up24_1.csv', index=False)
    m_up24_2.to_csv(
        'processed_data/m_up24_2.csv', index=False)
    m_up24_3.to_csv(
        'processed_data/m_up24_3.csv', index=False)
    m_up24_4.to_csv(
        'processed_data/m_up24_4.csv', index=False)
    m_up24_5.to_csv(
        'processed_data/m_up24_5.csv', index=False)

    m_down24_1.to_csv(
        'processed_data/m_down24_1.csv', index=False)
    m_down24_2.to_csv(
        'processed_data/m_down24_2.csv', index=False)
    m_down24_3.to_csv(
        'processed_data/m_down24_3.csv', index=False)
    m_down24_4.to_csv(
        'processed_data/m_down24_4.csv', index=False)
    m_down24_5.to_csv(
        'processed_data/m_down24_5.csv', index=False)

    d_run_4min.to_csv(
        'processed_data/d_run_4min.csv', index=False)

    d_up_1.to_csv(
        'processed_data/d_up_1.csv', index=False)
    d_up_2.to_csv(
        'processed_data/d_up_2.csv', index=False)
    d_up_3.to_csv(
        'processed_data/d_up_3.csv', index=False)
    d_up_4.to_csv(
        'processed_data/d_up_4.csv', index=False)

    d_down_1.to_csv(
        'processed_data/d_down_1.csv', index=False)
    d_down_2.to_csv(
        'processed_data/d_down_2.csv', index=False)
    d_down_3.to_csv(
        'processed_data/d_down_3.csv', index=False)
    d_down_4.to_csv(
        'processed_data/d_down_4.csv', index=False)

    dlp_upstairs_1.to_csv('processed_data/dlp_upstairs_1.csv', index=False)
    dlp_upstairs_2.to_csv('processed_data/dlp_upstairs_2.csv', index=False)
    dlp_downstairs_1.to_csv('processed_data/dlp_downstairs_1.csv', index=False)
    dlp_downstairs_2.to_csv('processed_data/dlp_downstairs_2.csv', index=False)

    s_up_1 = process_file('data/s_up_0.csv').to_csv('processed_data/srp_up_1.csv', index=False)
    s_up_2 = process_file('data/s_up_1.csv').to_csv('processed_data/srp_up_2.csv', index=False)
    s_up_3 = process_file('data/s_up_2.csv').to_csv('processed_data/srp_up_3.csv', index=False)
    s_up_4 = process_file('data/s_up_3.csv').to_csv('processed_data/srp_up_4.csv', index=False)
    s_up_5 = process_file('data/s_up_4.csv').to_csv('processed_data/srp_up_5.csv', index=False)
    s_up_6 = process_file('data/s_up_5.csv').to_csv('processed_data/srp_up_6.csv', index=False)
    s_up_7 = process_file('data/s_up_6.csv').to_csv('processed_data/srp_up_7.csv', index=False)
    s_up_8 = process_file('data/s_up_7.csv').to_csv('processed_data/srp_up_8.csv', index=False)
    s_up_9 = process_file('data/s_up_8.csv').to_csv('processed_data/srp_up_9.csv', index=False)
    s_up_10 = process_file('data/s_up_9.csv').to_csv('processed_data/srp_up_10.csv', index=False)

    s_down_1 = process_file('data/s_down_0.csv').to_csv('processed_data/srp_down_1.csv', index=False)
    s_down_2 = process_file('data/s_down_1.csv').to_csv('processed_data/srp_down_2.csv', index=False)
    s_down_3 = process_file('data/s_down_2.csv').to_csv('processed_data/srp_down_3.csv', index=False)
    s_down_4 = process_file('data/s_down_3.csv').to_csv('processed_data/srp_down_4.csv', index=False)
    s_down_5 = process_file('data/s_down_4.csv').to_csv('processed_data/srp_down_5.csv', index=False)
    s_down_6 = process_file('data/s_down_5.csv').to_csv('processed_data/srp_down_6.csv', index=False)
    s_down_7 = process_file('data/s_down_6.csv').to_csv('processed_data/srp_down_7.csv', index=False)
    s_down_8 = process_file('data/s_down_7.csv').to_csv('processed_data/srp_down_8.csv', index=False)
    s_down_9 = process_file('data/s_down_8.csv').to_csv('processed_data/srp_down_9.csv', index=False)
    s_down_10 = process_file('data/s_down_9.csv').to_csv('processed_data/srp_down_10.csv', index=False)

    
if __name__ == "__main__":
    main()
