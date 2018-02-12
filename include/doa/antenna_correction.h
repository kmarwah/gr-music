/* -*- c++ -*- */
/*
 * Copyright 2018
 * Kabir Marwah <km3415@ic.ac.uk>
 */

#ifndef INCLUDED_DOA_ANTENNA_CORRECTION_H
#define INCLUDED_DOA_ANTENNA_CORRECTION_H

#include <doa/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace doa {

    /*!
     * \brief Performs a scaling operation on a correlation matrix.
     * \ingroup doa
     * 
     * \details
     * This block takes a correlation matrix of size (number of antenna elements x number of antenna elements) 
     * as input and multiplies it with a diagonal matrix of size (number of antenna elements x number of antenna elements) 
     * using calibration values retrieved from a config file. 
     */
    class DOA_API antenna_correction : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<antenna_correction> sptr;

      /*!
       * \brief Make a block to correct a correlation matrix for non-uniform antenna gain and phase. 
       *
       * \param num_ant_ele     Number of antenna elements
       * \param config_filename Config file consisting of antenna calibration values
       */
      static sptr make(int num_ant_ele, char* config_filename);
    };

  } // namespace doa
} // namespace gr

#endif /* INCLUDED_DOA_ANTENNA_CORRECTION_H */

