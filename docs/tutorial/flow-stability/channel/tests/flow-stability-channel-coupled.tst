<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Flow Stability, Channel, Stability, Coupled</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>Channel-Coupled.xml</parameters>
    <files>
        <file description="Session File">../flow-stability-channel/completed/stability/Coupled/Channel-Coupled.xml</file>
        <file description="Baseflow File">../flow-stability-channel/completed/stability/Coupled/Channel-Coupled.bse</file>
    </files>
    <metrics>
        <metric type="Eigenvalue" id="0">
            <value tolerance="0.001">0.00223509,0.249891</value>
            <value tolerance="0.001">0.00223509,-0.249891</value>
        </metric>
    </metrics>
</test>
