<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Flow Stability, Cylinder, Stability, Adjoint</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>Cylinder_Adjoint.xml</parameters>
    <files>
        <file description="Session File">../flow-stability-cylinder/completed/stability/Adjoint/Cylinder_Adjoint.xml</file>
        <file description="Baseflow File">../flow-stability-cylinder/completed/stability/Adjoint/Cylinder_Adjoint.bse</file>
        <file description="Restart File">../flow-stability-cylinder/completed/stability/Adjoint/Cylinder_Adjoint.rst</file>
    </files>
    <metrics>
        <metric type="Eigenvalue" id="0">
            <value tolerance="0.001">0.980493,0.727526</value>
            <value tolerance="0.001">0.980493,-0.727526</value>
        </metric>
    </metrics>
</test>
