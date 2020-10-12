///////////////////////////////////////////////////////////////////////////////
//
// File NektarUnivConsts.hpp
//
// For more information, please see: http://www.nektar.info
//
// The MIT License
//
// Copyright (c) 2006 Scientific Computing and Imaging Institute,
// University of Utah (USA) and Department of Aeronautics, Imperial
// College London (UK).
//
// Permission is hereby granted, free of charge, to any person obtaining a
// copy of this software and associated documentation files (the "Software"),
// to deal in the Software without restriction, including without limitation
// the rights to use, copy, modify, merge, publish, distribute, sublicense,
// and/or sell copies of the Software, and to permit persons to whom the
// Software is furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included
// in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
// OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
// THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
// FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
// DEALINGS IN THE SOFTWARE.
//
// Description: Universal constants in the Nektar Library
//
///////////////////////////////////////////////////////////////////////////////

#ifndef  NEKTARUNIVCONSTS_HPP
#define  NEKTARUNIVCONSTS_HPP

#include <limits>

#include <LibUtilities/BasicConst/NektarUnivTypeDefs.hpp>

namespace Nektar
{
    namespace NekConstants
    {
        static constexpr NekDouble kNekUnsetDouble = -9999;
        static constexpr NekDouble kNekMinResidInit = 1e16;
        static constexpr NekDouble kVertexTheSameDouble  = 1.0e-8;
        static constexpr NekDouble kGeomFactorsTol = 1.0e-8;
        static constexpr NekDouble kNekZeroTol = 1.0e-12;
        static constexpr NekDouble kGeomRightAngleTol = 1e-14;
        static constexpr NekDouble kNekSqrtTol = 1.0e-16;
        static constexpr NekDouble kNekIterativeTol = 1e-09;
        static constexpr NekDouble kNekSparseNonZeroTol = 1e-16;

        // Tolerances for mesh generation and CAD handling
        static constexpr NekDouble GeomTol = 1E-2;
        static constexpr NekDouble CoinTol = 1E-6;

        // Factor for tolerance for floating point comparison
        static constexpr unsigned int kNekFloatCompFact = 4;
    }
} //end of namespace

#endif
