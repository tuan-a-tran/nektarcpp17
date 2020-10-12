///////////////////////////////////////////////////////////////////////////////
//
// File: CompressibleSolver.h
//
// For more information, please see: http://www.nektar.info
//
// The MIT License
//
// Copyright (c) 2006 Division of Applied Mathematics, Brown University (USA),
// Department of Aeronautics, Imperial College London (UK), and Scientific
// Computing and Imaging Institute, University of Utah (USA).
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
// Description: Compressible Riemann solver.
//
///////////////////////////////////////////////////////////////////////////////

#ifndef NEKTAR_SOLVERS_COMPRESSIBLEFLOWSOLVER_RIEMANNSOLVER_COMPRESSIBLESOLVER
#define NEKTAR_SOLVERS_COMPRESSIBLEFLOWSOLVER_RIEMANNSOLVER_COMPRESSIBLESOLVER

#include <SolverUtils/RiemannSolvers/RiemannSolver.h>
#include <CompressibleFlowSolver/Misc/EquationOfState.h>

using namespace Nektar::SolverUtils;

namespace Nektar
{
    class CompressibleSolver : public RiemannSolver
    {
    protected:
        bool m_pointSolve;
        EquationOfStateSharedPtr m_eos;
        bool m_idealGas;
        
        CompressibleSolver(
                const LibUtilities::SessionReaderSharedPtr& pSession);

        virtual void v_Solve(
            const int                                         nDim,
            const Array<OneD, const Array<OneD, NekDouble> > &Fwd,
            const Array<OneD, const Array<OneD, NekDouble> > &Bwd,
                  Array<OneD,       Array<OneD, NekDouble> > &flux);

        virtual void v_ArraySolve(
            [[maybe_unused]] const Array<OneD, const Array<OneD, NekDouble> > &Fwd,
            [[maybe_unused]] const Array<OneD, const Array<OneD, NekDouble> > &Bwd,
                  [[maybe_unused]] Array<OneD,       Array<OneD, NekDouble> > &flux,
            [[maybe_unused]] const int nDim)
        {
            NEKERROR(ErrorUtil::efatal,
                     "This function should be defined by subclasses.");
        }
        
        virtual void v_PointSolve(
            [[maybe_unused]] NekDouble  rhoL, [[maybe_unused]] NekDouble  rhouL, 
            [[maybe_unused]] NekDouble  rhovL, [[maybe_unused]] NekDouble  rhowL, [[maybe_unused]] NekDouble  EL,
            [[maybe_unused]] NekDouble  rhoR, [[maybe_unused]] NekDouble  rhouR, 
            [[maybe_unused]] NekDouble  rhovR, [[maybe_unused]] NekDouble  rhowR, [[maybe_unused]] NekDouble  ER,
            [[maybe_unused]] NekDouble &rhof, [[maybe_unused]] NekDouble &rhouf, 
            [[maybe_unused]] NekDouble &rhovf, [[maybe_unused]] NekDouble &rhowf, [[maybe_unused]] NekDouble &Ef)
        {
            NEKERROR(ErrorUtil::efatal,
                     "This function should be defined by subclasses.");
        }

        virtual void v_PointSolveVisc(
            [[maybe_unused]] NekDouble  rhoL, [[maybe_unused]] NekDouble  rhouL, 
            [[maybe_unused]] NekDouble  rhovL, [[maybe_unused]] NekDouble  rhowL, 
            [[maybe_unused]] NekDouble  EL, [[maybe_unused]] NekDouble EpsL,
            [[maybe_unused]] NekDouble  rhoR, [[maybe_unused]] NekDouble  rhouR, 
            [[maybe_unused]] NekDouble  rhovR, [[maybe_unused]] NekDouble  rhowR, 
            [[maybe_unused]] NekDouble  ER, [[maybe_unused]] NekDouble EpsR,
            [[maybe_unused]] NekDouble &rhof, [[maybe_unused]] NekDouble &rhouf, 
            [[maybe_unused]] NekDouble &rhovf, [[maybe_unused]] NekDouble &rhowf, 
            [[maybe_unused]] NekDouble &Ef, [[maybe_unused]] NekDouble &Epsf)
        {
            NEKERROR(ErrorUtil::efatal,
                     "This function should be defined by subclasses.");
        }

        NekDouble GetRoeSoundSpeed(
            NekDouble rhoL, NekDouble pL, NekDouble eL, NekDouble HL, NekDouble srL,
            NekDouble rhoR, NekDouble pR, NekDouble eR, NekDouble HR, NekDouble srR,
            NekDouble HRoe, NekDouble URoe2, NekDouble srLR);
    };
}

#endif
