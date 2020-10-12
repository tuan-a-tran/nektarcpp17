<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Flow Stability, Cylinder, Stability, Direct</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>Cylinder_Direct.xml</parameters>
    <files>
        <file description="Session File">../flow-stability-cylinder/completed/stability/Direct/Cylinder_Direct.xml</file>
        <file description="Baseflow File">../flow-stability-cylinder/completed/stability/Direct/Cylinder_Direct.bse</file>
        <file description="Restart File">../flow-stability-cylinder/completed/stability/Direct/Cylinder_Direct.rst</file>
    </files>
    <metrics>
        <metric type="Eigenvalue" id="0">
            <value tolerance="0.001">0.9792,0.726586</value>
            <value tolerance="0.001">0.9792,-0.726586</value>
        </metric>
    </metrics>
</test>
