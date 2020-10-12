<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Flow Stability, Channel, Stability, VCS</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>Channel-VCS.xml</parameters>
    <files>
        <file description="Session File">../flow-stability-channel/completed/stability/VCS/Channel-VCS.xml</file>
        <file description="Baseflow File">../flow-stability-channel/completed/stability/VCS/Channel-VCS.bse</file>
        <file description="Restart File">../flow-stability-channel/completed/stability/VCS/Channel-VCS.rst</file>
    </files>
    <metrics>
        <metric type="Eigenvalue" id="0">
            <value tolerance="0.001">1.00112,0.124946</value>
            <value tolerance="0.001">1.00112,-0.124946</value>
        </metric>
    </metrics>
</test>
