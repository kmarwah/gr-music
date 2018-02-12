/* -*- c++ -*- */
/*
 * Copyright 2018
 * Kabir Marwah <km3415@ic.ac.uk>
 */


#ifndef INCLUDED_DOA_ROOTMUSIC_LINEAR_ARRAY_H
#define INCLUDED_DOA_ROOTMUSIC_LINEAR_ARRAY_H

#include <doa/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace doa {

    /*!
     * \brief Performs DoA estimation using Root-MUSIC algorithm for a linear antenna array. 
     * \ingroup doa
     * 
     * \details
     * This block takes a correlation matrix of size (number of antenna elements x number of antenna elements) 
     * as input and generates a complex vector of size (pseudo-spectrum length x 1) 
     * whose arg-max values represent the estimated DoAs. 
     */
    class DOA_API rootMUSIC_linear_array : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<rootMUSIC_linear_array> sptr;

      /*!
       * \brief Make a block to estimate DoAs using Root-MUSIC algorithm for linear arrays.
       *
       * \param norm_spacing    Normalized spacing between antenna elements
       * \param num_targets     Known number of targets 
       * \param num_ant_ele     Number of antenna elements
       */
      static sptr make(float norm_spacing, int num_targets, int num_ant_ele);
    };

  } // namespace doa
} // namespace gr

#endif /* INCLUDED_DOA_ROOTMUSIC_LINEAR_ARRAY_H */

