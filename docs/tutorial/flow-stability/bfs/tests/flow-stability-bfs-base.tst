<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Flow Stability, BFS, Base flow</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>-P NumSteps=500 bfs-Base.xml</parameters>
    <files>
        <file description="Session File">../flow-stability-bfs/completed/base/bfs-Base.xml</file>
    </files>
    <metrics>
        <metric type="L2" id="1">
            <value variable="u" tolerance="1e-3">4.0396</value>
            <value variable="v" tolerance="1e-3">0.246488</value>
            <value variable="p" tolerance="1e-3">3.14456</value>
        </metric>
        <metric type="Linf" id="2">
            <value variable="u" tolerance="1e-3">1</value>
            <value variable="v" tolerance="1e-3">0.623913</value>
            <value variable="p" tolerance="1e-3">0.660293</value>
        </metric>
    </metrics>
</test>
