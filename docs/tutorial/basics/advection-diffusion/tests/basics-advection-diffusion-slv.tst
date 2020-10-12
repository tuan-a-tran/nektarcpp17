<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>ADR Solver, advection diffusion DG</description>
    <parameters>ADR_mesh_aligned.xml ADR_conditions.xml</parameters>
    <files>
        <file description="Session File">../basics-advection-diffusion/completed/ADR_mesh_aligned.xml</file>
        <file description="Session File">../basics-advection-diffusion/completed/ADR_conditions.xml</file>
    </files>
    <metrics>
        <metric type="L2" id="1">
            <value variable="u" tolerance="1e-8">0.00863475</value>
        </metric>
        <metric type="Linf" id="2">
            <value variable="u" tolerance="1e-8">0.0390366</value>
        </metric>
    </metrics>
</test>
