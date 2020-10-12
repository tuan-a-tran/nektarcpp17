<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>ADR Solver, align xml to be periodic</description>
    <parameters> -m peralign:surf1=200:surf2=400:dir=x -m jac:list ADR_mesh.xml ADR_mesh_aligned.xml </parameters>
    <files>
        <file description="Input File">../basics-advection-diffusion/completed/ADR_mesh.xml</file>
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
