<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>ADR Solver, helmholtz</description>
    <parameters>Helm_mesh.xml Helm_conditions.xml</parameters>
    <files>
        <file description="Session File">../basics-helmholtz/completed/Helm_mesh.xml</file>
        <file description="Session File">../basics-helmholtz/completed/Helm_conditions.xml</file>
    </files>
    <metrics>
        <metric type="L2" id="1">
            <value variable="u" tolerance="1e-8">0.000159378</value>
        </metric>
        <metric type="Linf" id="2">
            <value variable="u" tolerance="1e-8">0.000454467</value>
        </metric>
    </metrics>
</test>
