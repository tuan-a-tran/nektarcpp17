<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Flow Stability, Cylinder, Base flow</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>Cylinder-Base.xml</parameters>
    <files>
        <file description="Session File">../flow-stability-cylinder/completed/base/Cylinder-Base.xml</file>
        <file description="Restart File">../flow-stability-cylinder/completed/base/Cylinder-Base.bse</file>
    </files>
    <metrics>
        <metric type="L2" id="1">
            <value variable="u" tolerance="1e-2">123.79</value>
            <value variable="v" tolerance="1e-3">0.893423</value>
            <value variable="p" tolerance="1e-3">1.13864</value>
        </metric>
        <metric type="Linf" id="2">
            <value variable="u" tolerance="1e-3">1.15536</value>
            <value variable="v" tolerance="1e-3">0.547215</value>
            <value variable="p" tolerance="1e-3">0.578963</value>
        </metric>
    </metrics>
</test>
