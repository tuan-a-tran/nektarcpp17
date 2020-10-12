<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>ADR Solver, convert gmsh to xml</description>
    <parameters> -m jac:list ADR_mesh.msh ADR_mesh.xml</parameters>
    <files>
        <file description="Input File">../basics-advection-diffusion/completed/ADR_mesh.msh</file>
    </files>
    <metrics>
        <metric type="regex" id="1">
            <regex>^Total negative Jacobians: (\d+)</regex>
            <matches>
                <match>
                    <field id="0">0</field>
                </match>
            </matches>
        </metric        >
    </metrics>          
</test>                 
