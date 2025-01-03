#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Digital_modulation
# Author: Saad
# GNU Radio version: v3.10.0.0git-632-g04cf420f

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio import zeromq
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import transmitter_v1_epy_block_0 as epy_block_0  # embedded python block



from gnuradio import qtgui

class transmitter_v1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Digital_modulation", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Digital_modulation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "transmitter_v1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.select_stream = select_stream = 0
        self.samp_rate = samp_rate = 1e6
        self.phase_cor = phase_cor = 0
        self.TX_gain = TX_gain = 28
        self.RX_gain = RX_gain = 28
        self.QPSK = QPSK = digital.constellation_calcdist([1, 1j, -1, -1j], [0, 1, 2, 3],
        4, 1, digital.constellation.NO_NORMALIZATION).base()
        self.QAM64 = QAM64 = digital.constellation_calcdist([-7.0000+7.0000j,-7.0000+5.0000j,-7.0000+1.0000j,-7.0000+3.0000j,-7.0000-7.0000j,-7.0000-5.0000j,-7.0000-1.0000j,-7.0000-3.0000j,-5.0000+7.0000j,-5.0000+5.0000j,-5.0000+1.0000j,-5.0000+3.0000j,-5.0000-7.0000j,-5.0000-5.0000j,-5.0000-1.0000j,-5.0000-3.0000j,-1.0000+7.0000j,-1.0000+5.0000j,-1.0000+1.0000j,-1.0000+3.0000j,-1.0000-7.0000j,-1.0000-5.0000j,-1.0000-1.0000j,-1.0000-3.0000j,-3.0000+7.0000j,-3.0000+5.0000j,-3.0000+1.0000j,-3.0000+3.0000j,-3.0000-7.0000j,-3.0000-5.0000j,-3.0000-1.0000j,-3.0000-3.0000j,7.0000+7.0000j,7.0000+5.0000j,7.0000+1.0000j,7.0000+3.0000j,7.0000-7.0000j,7.0000-5.0000j,7.0000-1.0000j,7.0000-3.0000j,5.0000+7.0000j,5.0000+5.0000j,5.0000+1.0000j,5.0000+3.0000j,5.0000-7.0000j,5.0000-5.0000j,5.0000-1.0000j,5.0000-3.0000j,1.0000+7.0000j,1.0000+5.0000j,1.0000+1.0000j,1.0000+3.0000j,1.0000-7.0000j,1.0000-5.0000j,1.0000-1.0000j,1.0000-3.0000j,3.0000+7.0000j,3.0000+5.0000j,3.0000+1.0000j,3.0000+3.0000j,3.0000-7.0000j,3.0000-5.0000j,3.0000-1.0000j,3.0000-3.0000j], [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63],
        4, 1, digital.constellation.NO_NORMALIZATION).base()
        self.QAM32 = QAM32 = digital.constellation_calcdist([-3.0000+5.0000j,-1.0000+5.0000j,-3.0000-5.0000j,-1.0000-5.0000j,-5.0000+3.0000j,-5.0000+1.0000j,-5.0000-3.0000j,-5.0000-1.0000j,
        -1.0000+3.0000j,-1.0000+1.0000j,-1.0000-3.0000j,-1.0000-1.0000j,-3.0000+3.0000j,-3.0000+1.0000j,-3.0000-3.0000j,-3.0000-1.0000j,
        3.0000+5.0000j,1.0000+5.0000j,3.0000-5.0000j,1.0000-5.0000j,5.0000+3.0000j,5.0000+1.0000j,5.0000-3.0000j,5.0000-1.0000j,
        1.0000+3.0000j,1.0000+1.0000j,1.0000-3.0000j,1.0000-1.0000j,3.0000+3.0000j,3.0000+1.0000j,3.0000-3.0000j,3.0000-1.0000j], [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        4, 1, digital.constellation.NO_NORMALIZATION).base()
        self.QAM16 = QAM16 = digital.constellation_calcdist([-3.0000 + 3.0000j,  -3.0000 + 1.0000j,  -3.0000 - 3.0000j,  -3.0000 - 1.0000j, -1.0000 + 3.0000j,  -1.0000 + 1.0000j,  -1.0000 - 3.0000j,  -1.0000 - 1.0000j, 3.0000 + 3.0000j,   3.0000 + 1.0000j,   3.0000 - 3.0000j,   3.0000 - 1.0000j, 1.0000 + 3.0000j,   1.0000 + 1.0000j,   1.0000 - 3.0000j,   1.0000 - 1.0000j], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        4, 1, digital.constellation.NO_NORMALIZATION).base()
        self.PSK8 = PSK8 = digital.constellation_calcdist([1.0000 + 0.0000j, 0.7071 + 0.7071j, 0.0000 + 1.0000j, -0.7071 + 0.7071j, -1.0000 + 0.0000j, -0.7071 - 0.7071j, 0.0000 - 1.0000j, 0.7071 - 0.7071j], [0, 1, 2, 3, 4, 5, 6, 7],
        4, 1, digital.constellation.NO_NORMALIZATION).base()
        self.PSK16 = PSK16 = digital.constellation_calcdist([1.0000+0.0000j, 0.9239+0.3827j, 0.7071+0.7071j, 0.3827+0.9239j, 0.0000+1.0000j, -0.3827+0.9238j, -0.7071+0.7071j, -0.9239+0.3827j, -1.0000+0.0000j, -0.9239-0.3827j, -0.7071-0.7071j, -0.3827-0.9239j, 0.0000-1.0000j, 0.3827-0.9239j, 0.7071-0.7071j, 0.9239-0.3827j], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        4, 1, digital.constellation.NO_NORMALIZATION).base()
        self.Noise_Profile = Noise_Profile = -10.0
        self.Int_gain = Int_gain = 0.5
        self.BPSK = BPSK = digital.constellation_calcdist([1, -1], [0, 1],
        4, 1, digital.constellation.NO_NORMALIZATION).base()

        ##################################################
        # Blocks
        ##################################################
        # Create the options list
        self._select_stream_options = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        # Create the labels list
        self._select_stream_labels = ['BPSK', 'QPSK', 'PSK8', 'PSK16', 'QAM16', 'QAM32', 'QAM64', 'NULL', 'Sine']
        # Create the combo box
        # Create the radio buttons
        self._select_stream_group_box = Qt.QGroupBox("Select Modulation" + ": ")
        self._select_stream_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._select_stream_button_group = variable_chooser_button_group()
        self._select_stream_group_box.setLayout(self._select_stream_box)
        for i, _label in enumerate(self._select_stream_labels):
            radio_button = Qt.QRadioButton(_label)
            self._select_stream_box.addWidget(radio_button)
            self._select_stream_button_group.addButton(radio_button, i)
        self._select_stream_callback = lambda i: Qt.QMetaObject.invokeMethod(self._select_stream_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._select_stream_options.index(i)))
        self._select_stream_callback(self.select_stream)
        self._select_stream_button_group.buttonClicked[int].connect(
            lambda i: self.set_select_stream(self._select_stream_options[i]))
        self.top_grid_layout.addWidget(self._select_stream_group_box, 0, 0, 1, 3)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._phase_cor_range = Range(0, 6.28, 0.01, 0, 200)
        self._phase_cor_win = RangeWidget(self._phase_cor_range, self.set_phase_cor, "phase_cor", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._phase_cor_win, 10, 0, 1, 3)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._TX_gain_range = Range(0, 31.5, 0.5, 28, 200)
        self._TX_gain_win = RangeWidget(self._TX_gain_range, self.set_TX_gain, "TX", "counter", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._TX_gain_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._RX_gain_range = Range(0, 31.5, 0.5, 28, 200)
        self._RX_gain_win = RangeWidget(self._RX_gain_range, self.set_RX_gain, "RX", "counter", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._RX_gain_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Noise_Profile_range = Range(-500, 500, 0.01, -10.0, 100000)
        self._Noise_Profile_win = RangeWidget(self._Noise_Profile_range, self.set_Noise_Profile, "Noise_floor", "counter", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Noise_Profile_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._Int_gain_range = Range(0, 1, 0.1, 0.5, 200)
        self._Int_gain_win = RangeWidget(self._Int_gain_range, self.set_Int_gain, "Internal gain", "counter", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._Int_gain_win, 2, 2, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.zeromq_pub_sink_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://127.0.0.1:55555', 100, False, -1, '')
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "addr=192.168.10.4")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        # No synchronization enforced.

        self.uhd_usrp_source_0.set_center_freq(3e9, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_gain(RX_gain, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", "addr=192.168.10.5")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_clock_source('mimo', 0)
        self.uhd_usrp_sink_0.set_time_source('mimo', 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        # No synchronization enforced.

        self.uhd_usrp_sink_0.set_center_freq(3e9, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(TX_gain, 0)
        self.rational_resampler_xxx_0_0_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=25,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=25,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            8192, #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 7, 0, 3, 3)
        for r in range(7, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            40e3, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 3, 0, 3, 3)
        for r in range(3, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                15e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                20e3,
                1e3,
                window.WIN_HAMMING,
                6.76))
        self.fft_vxx_0 = fft.fft_vcc(4096, True, [], True, 1)
        self.epy_block_0 = epy_block_0.blk(n=4096)
        self.digital_constellation_modulator_0_0_1 = digital.generic_mod(
            constellation=PSK8,
            differential=True,
            samples_per_symbol=16,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=True)
        self.digital_constellation_modulator_0_0_0_2 = digital.generic_mod(
            constellation=QAM32,
            differential=True,
            samples_per_symbol=16,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=True)
        self.digital_constellation_modulator_0_0_0_1 = digital.generic_mod(
            constellation=QAM64,
            differential=True,
            samples_per_symbol=16,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=True)
        self.digital_constellation_modulator_0_0_0_0 = digital.generic_mod(
            constellation=QAM16,
            differential=True,
            samples_per_symbol=16,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=True)
        self.digital_constellation_modulator_0_0_0 = digital.generic_mod(
            constellation=PSK16,
            differential=True,
            samples_per_symbol=16,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=True)
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=QPSK,
            differential=True,
            samples_per_symbol=16,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=True)
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=BPSK,
            differential=True,
            samples_per_symbol=16,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False,
            truncate=True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 4096)
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,select_stream,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_phase_shift_0 = blocks.phase_shift(phase_cor, True)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_ff(0.000244*0.000244, 4096)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(Int_gain)
        self.blocks_multiply_const_vxx_0_5 = blocks.multiply_const_cc(1)
        self.blocks_multiply_const_vxx_0_4 = blocks.multiply_const_cc(1)
        self.blocks_multiply_const_vxx_0_3 = blocks.multiply_const_cc(1)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_cc(1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_cc(0.3162)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(0.2236)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(0.1543)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(4096)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(Noise_Profile*-1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate/25, analog.GR_COS_WAVE, 1000, 1, 0, 0)
        self.analog_random_uniform_source_x_0_0_3 = analog.random_uniform_source_b(0, 255, 0)
        self.analog_random_uniform_source_x_0_0_2 = analog.random_uniform_source_b(0, 255, 0)
        self.analog_random_uniform_source_x_0_0_1 = analog.random_uniform_source_b(0, 255, 0)
        self.analog_random_uniform_source_x_0_0_0_0 = analog.random_uniform_source_b(0, 255, 0)
        self.analog_random_uniform_source_x_0_0_0 = analog.random_uniform_source_b(0, 255, 0)
        self.analog_random_uniform_source_x_0_0 = analog.random_uniform_source_b(0, 255, 0)
        self.analog_random_uniform_source_x_0 = analog.random_uniform_source_b(0, 255, 0)
        self.analog_const_source_x_1 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.SNR = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.SNR.set_update_time(0.10)
        self.SNR.set_title('SNR')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.SNR.set_min(i, -1)
            self.SNR.set_max(i, 1)
            self.SNR.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.SNR.set_label(i, "Data {0}".format(i))
            else:
                self.SNR.set_label(i, labels[i])
            self.SNR.set_unit(i, units[i])
            self.SNR.set_factor(i, factor[i])

        self.SNR.enable_autoscale(False)
        self._SNR_win = sip.wrapinstance(self.SNR.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._SNR_win, 6, 0, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.Ess_Total_Power_dB = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.Ess_Total_Power_dB.set_update_time(0.10)
        self.Ess_Total_Power_dB.set_title('Ess_Total_Power_dB')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Ess_Total_Power_dB.set_min(i, -1000)
            self.Ess_Total_Power_dB.set_max(i, 1000)
            self.Ess_Total_Power_dB.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Ess_Total_Power_dB.set_label(i, "Data {0}".format(i))
            else:
                self.Ess_Total_Power_dB.set_label(i, labels[i])
            self.Ess_Total_Power_dB.set_unit(i, units[i])
            self.Ess_Total_Power_dB.set_factor(i, factor[i])

        self.Ess_Total_Power_dB.enable_autoscale(False)
        self._Ess_Total_Power_dB_win = sip.wrapinstance(self.Ess_Total_Power_dB.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Ess_Total_Power_dB_win, 6, 2, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.Ess_Total_Power = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1,
            None # parent
        )
        self.Ess_Total_Power.set_update_time(0.10)
        self.Ess_Total_Power.set_title('Ess_Total_Power')

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.Ess_Total_Power.set_min(i, -1000)
            self.Ess_Total_Power.set_max(i, 1000)
            self.Ess_Total_Power.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.Ess_Total_Power.set_label(i, "Data {0}".format(i))
            else:
                self.Ess_Total_Power.set_label(i, labels[i])
            self.Ess_Total_Power.set_unit(i, units[i])
            self.Ess_Total_Power.set_factor(i, factor[i])

        self.Ess_Total_Power.enable_autoscale(False)
        self._Ess_Total_Power_win = sip.wrapinstance(self.Ess_Total_Power.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Ess_Total_Power_win, 6, 1, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_selector_0, 7))
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_random_uniform_source_x_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.analog_random_uniform_source_x_0_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.analog_random_uniform_source_x_0_0_0, 0), (self.digital_constellation_modulator_0_0_0_2, 0))
        self.connect((self.analog_random_uniform_source_x_0_0_0_0, 0), (self.digital_constellation_modulator_0_0_0_1, 0))
        self.connect((self.analog_random_uniform_source_x_0_0_1, 0), (self.digital_constellation_modulator_0_0_0_0, 0))
        self.connect((self.analog_random_uniform_source_x_0_0_2, 0), (self.digital_constellation_modulator_0_0_1, 0))
        self.connect((self.analog_random_uniform_source_x_0_0_3, 0), (self.digital_constellation_modulator_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0, 8))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.SNR, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_selector_0, 6))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_selector_0, 5))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_selector_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_selector_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_3, 0), (self.blocks_selector_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_4, 0), (self.blocks_selector_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_5, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.Ess_Total_Power_dB, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_phase_shift_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_phase_shift_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_selector_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_multiply_const_vxx_0_2, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.blocks_multiply_const_vxx_0_5, 0))
        self.connect((self.digital_constellation_modulator_0_0_0, 0), (self.blocks_multiply_const_vxx_0_4, 0))
        self.connect((self.digital_constellation_modulator_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.digital_constellation_modulator_0_0_0_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_constellation_modulator_0_0_0_2, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.digital_constellation_modulator_0_0_1, 0), (self.blocks_multiply_const_vxx_0_3, 0))
        self.connect((self.epy_block_0, 0), (self.Ess_Total_Power, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0_0, 0), (self.zeromq_pub_sink_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_phase_shift_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "transmitter_v1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_select_stream(self):
        return self.select_stream

    def set_select_stream(self, select_stream):
        self.select_stream = select_stream
        self._select_stream_callback(self.select_stream)
        self.blocks_selector_0.set_input_index(self.select_stream)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate/25)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 20e3, 1e3, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 15e3, 1e3, window.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_phase_cor(self):
        return self.phase_cor

    def set_phase_cor(self, phase_cor):
        self.phase_cor = phase_cor
        self.blocks_phase_shift_0.set_shift(self.phase_cor)

    def get_TX_gain(self):
        return self.TX_gain

    def set_TX_gain(self, TX_gain):
        self.TX_gain = TX_gain
        self.uhd_usrp_sink_0.set_gain(self.TX_gain, 0)

    def get_RX_gain(self):
        return self.RX_gain

    def set_RX_gain(self, RX_gain):
        self.RX_gain = RX_gain
        self.uhd_usrp_source_0.set_gain(self.RX_gain, 0)

    def get_QPSK(self):
        return self.QPSK

    def set_QPSK(self, QPSK):
        self.QPSK = QPSK

    def get_QAM64(self):
        return self.QAM64

    def set_QAM64(self, QAM64):
        self.QAM64 = QAM64

    def get_QAM32(self):
        return self.QAM32

    def set_QAM32(self, QAM32):
        self.QAM32 = QAM32

    def get_QAM16(self):
        return self.QAM16

    def set_QAM16(self, QAM16):
        self.QAM16 = QAM16

    def get_PSK8(self):
        return self.PSK8

    def set_PSK8(self, PSK8):
        self.PSK8 = PSK8

    def get_PSK16(self):
        return self.PSK16

    def set_PSK16(self, PSK16):
        self.PSK16 = PSK16

    def get_Noise_Profile(self):
        return self.Noise_Profile

    def set_Noise_Profile(self, Noise_Profile):
        self.Noise_Profile = Noise_Profile
        self.blocks_add_const_vxx_0.set_k(self.Noise_Profile*-1)

    def get_Int_gain(self):
        return self.Int_gain

    def set_Int_gain(self, Int_gain):
        self.Int_gain = Int_gain
        self.blocks_multiply_const_vxx_1.set_k(self.Int_gain)

    def get_BPSK(self):
        return self.BPSK

    def set_BPSK(self, BPSK):
        self.BPSK = BPSK




def main(top_block_cls=transmitter_v1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
