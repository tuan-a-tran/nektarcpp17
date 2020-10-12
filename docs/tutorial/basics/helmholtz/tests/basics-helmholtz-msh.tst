<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>ADR Solver, convert gmsh to xml</description>
    <parameters> -m jac:list Helm_mesh.msh Helm_mesh.xml</parameters>
    <files>
        <file description="Input File">../basics-helmholtz/completed/Helm_mesh.msh</file>
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
