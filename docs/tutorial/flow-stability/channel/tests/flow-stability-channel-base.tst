<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Flow Stability, Channel, Base flow</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>Channel-Base.xml</parameters>
    <files>
        <file description="Session File">../flow-stability-channel/completed/base/Channel-Base.xml</file>
    </files>
    <metrics>
        <metric type="L2" id="1">
            <value variable="u" tolerance="1e-8">1.78555e-12</value>
            <value variable="v" tolerance="1e-8">5.2462e-13</value>
            <value variable="p" tolerance="1e-8">1.5928e-11</value>
        </metric>
        <metric type="Linf" id="2">
            <value variable="u" tolerance="1e-8">4.61566e-12</value>
            <value variable="v" tolerance="1e-8">1.46721e-11</value>
            <value variable="p" tolerance="1e-8">5.85927e-12</value>
        </metric>
    </metrics>
</test>
