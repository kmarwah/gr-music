#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Calculate X310 Twinrx Phase Sync Accuracy
# Generated: Fri Feb  9 18:03:27 2018
##################################################

def struct(data): return type('Struct', (object,), data)()
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import doa
import os


class calculate_X310_TwinRX_phase_sync_accuracy(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Calculate X310 Twinrx Phase Sync Accuracy")

        ##################################################
        # Variables
        ##################################################
        self.input_variables = input_variables = struct({'SampleRate': 1000000, 'ToneFreq': 10000, 'CenterFreq': 2450000000, 'NumArrayElements': 4, 'Gain': 60, 'RxAddr': "addr=192.168.10.2", 'DirectoryConfigFiles': "/tmp", 'RelativePhaseOffsets': "measure_X310_TwinRX_relative_phase_offsets_245.cfg", 'CorrectedPhaseOffsets': "measure_X310_TwinRX_corrected_phase_offsets_245.cfg", 'SkipAhead': 2**13, 'Samples2FindMax': 2**11, })
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name = os.path.join(input_variables.DirectoryConfigFiles, input_variables.RelativePhaseOffsets)
        self.corrected_phase_offsets_file_name = corrected_phase_offsets_file_name = os.path.join(input_variables.DirectoryConfigFiles, input_variables.CorrectedPhaseOffsets)

        ##################################################
        # Blocks
        ##################################################
        self.twinrx_usrp_source_0 = doa.twinrx_usrp_source(
            samp_rate=input_variables.SampleRate,
            center_freq=input_variables.CenterFreq,
            gain=input_variables.Gain,
            sources=input_variables.NumArrayElements,
            addresses=input_variables.RxAddr
        )
        self.phase_correct_hier_1 = doa.phase_correct_hier(
            num_ports=input_variables.NumArrayElements,
            config_filename=rel_phase_offsets_file_name,
        )
        self.doa_twinrx_phase_offset_est_0 = doa.twinrx_phase_offset_est(input_variables.NumArrayElements, input_variables.SkipAhead)
        self.doa_findmax_and_save_0 = doa.findmax_and_save(input_variables.Samples2FindMax, input_variables.NumArrayElements-1, corrected_phase_offsets_file_name)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.doa_twinrx_phase_offset_est_0, 0), (self.doa_findmax_and_save_0, 0))    
        self.connect((self.doa_twinrx_phase_offset_est_0, 1), (self.doa_findmax_and_save_0, 1))    
        self.connect((self.doa_twinrx_phase_offset_est_0, 2), (self.doa_findmax_and_save_0, 2))    
        self.connect((self.phase_correct_hier_1, 0), (self.doa_twinrx_phase_offset_est_0, 0))    
        self.connect((self.phase_correct_hier_1, 1), (self.doa_twinrx_phase_offset_est_0, 1))    
        self.connect((self.phase_correct_hier_1, 2), (self.doa_twinrx_phase_offset_est_0, 2))    
        self.connect((self.phase_correct_hier_1, 3), (self.doa_twinrx_phase_offset_est_0, 3))    
        self.connect((self.twinrx_usrp_source_0, 0), (self.phase_correct_hier_1, 0))    
        self.connect((self.twinrx_usrp_source_0, 1), (self.phase_correct_hier_1, 1))    
        self.connect((self.twinrx_usrp_source_0, 2), (self.phase_correct_hier_1, 2))    
        self.connect((self.twinrx_usrp_source_0, 3), (self.phase_correct_hier_1, 3))    

    def get_input_variables(self):
        return self.input_variables

    def set_input_variables(self, input_variables):
        self.input_variables = input_variables

    def get_rel_phase_offsets_file_name(self):
        return self.rel_phase_offsets_file_name

    def set_rel_phase_offsets_file_name(self, rel_phase_offsets_file_name):
        self.rel_phase_offsets_file_name = rel_phase_offsets_file_name

    def get_corrected_phase_offsets_file_name(self):
        return self.corrected_phase_offsets_file_name

    def set_corrected_phase_offsets_file_name(self, corrected_phase_offsets_file_name):
        self.corrected_phase_offsets_file_name = corrected_phase_offsets_file_name


def main(top_block_cls=calculate_X310_TwinRX_phase_sync_accuracy, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
