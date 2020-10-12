<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description>NekMesh, cylinder mesh</description>
    <parameters> -m jac:list cyl.mcf cyl.xml</parameters>
    <files>
        <file description="Input File">../mesh-generation-2d-step/completed/cyl.mcf</file>
        <file description="Input File">../mesh-generation-2d-step/completed/cyl.stp</file>
    </files>
    <metrics>
        <metric type="regex" id="1">
            <regex>^Total negative Jacobians: (\d+)</regex>
            <matches>
                <match>
                    <field id="0">0</field>
                </match>
            </matches>
        </metric>
    </metrics>
</test>
