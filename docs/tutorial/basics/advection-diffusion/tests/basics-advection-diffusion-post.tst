<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>ADR Solver, post process fld </description>
    <parameters> -e ADR_mesh_aligned.xml ADR_conditions.xml ADR_mesh_aligned.fld ADR_mesh_aligned.dat</parameters>
    <files>
        <file description="Session File">../basics-advection-diffusion/completed/ADR_mesh_aligned.xml</file>
        <file description="Session File">../basics-advection-diffusion/completed/ADR_conditions.xml</file>
        <file description="Session File">../basics-advection-diffusion/completed/ADR_mesh_aligned.fld</file>
    </files>
    <metrics>
        <metric type="L2" id="1">
            <value variable="x" tolerance="1e-8">1.1547</value>
            <value variable="y" tolerance="1e-8">1.1547</value>
            <value variable="u" tolerance="1e-8">0.999236</value>
        </metric>
    </metrics>
</test>
