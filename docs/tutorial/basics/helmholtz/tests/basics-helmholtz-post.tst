<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>ADR Solver, post process fld </description>
    <parameters> -e Helm_mesh.xml Helm_conditions.xml Helm_mesh.fld Helm_mesh.dat</parameters>
    <files>
        <file description="Session File">../basics-helmholtz/completed/Helm_mesh.xml</file>
        <file description="Session File">../basics-helmholtz/completed/Helm_conditions.xml</file>
        <file description="Session File">../basics-helmholtz/completed/Helm_mesh.fld</file>
    </files>
    <metrics>
        <metric type="L2" id="1">
            <value variable="x" tolerance="1e-8">1.1547</value>
            <value variable="y" tolerance="1e-8">1.1547</value>
            <value variable="u" tolerance="1e-8">1.00002</value>
        </metric>
    </metrics>
</test>
