<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Inc N-S, TGV, 64 element</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>-P NumSteps=50 TGV64_mesh.xml TGV64_conditions.xml</parameters>
    <files>
        <file description="Session File">../incns-taylor-green-vortex/completed/solver64/TGV64_mesh.xml</file>
        <file description="Session File">../incns-taylor-green-vortex/completed/solver64/TGV64_conditions.xml</file>
    </files>
    <metrics>
        <metric type="L2" id="1">
            <value variable="u" tolerance="1e-4">3.91862</value>
            <value variable="v" tolerance="1e-4">3.91862</value>
            <value variable="w" tolerance="1e-4">0.486662</value>
            <value variable="p" tolerance="1e-4">3.14691</value>
        </metric>
        <metric type="Linf" id="2">
            <value variable="u" tolerance="1e-4">0.987583</value>
            <value variable="v" tolerance="1e-4">0.987583</value>
            <value variable="w" tolerance="1e-4">0.126036</value>
            <value variable="p" tolerance="1e-4">0.597182</value>
        </metric>
    </metrics>
</test>
