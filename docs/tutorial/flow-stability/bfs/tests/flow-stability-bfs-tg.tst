<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>Flow Stability, BFS, Transient Growth</description>
    <executable>IncNavierStokesSolver</executable>
    <parameters>bfs_tg.xml</parameters>
    <files>
        <file description="Session File">../flow-stability-bfs/completed/stability/bfs_tg.xml</file>
        <file description="Baseflow File">../flow-stability-bfs/completed/stability/bfs_tg.bse</file>
        <file description="Restart File">../flow-stability-bfs/completed/stability/bfs_tg.rst</file>
    </files>
    <metrics>
        <metric type="Eigenvalue" id="0">
            <value tolerance="0.001">3.23586,0</value>
        </metric>
    </metrics>
</test>
