<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description> StdIntegration1D tutorial  </description>
    <executable python="true"> StdIntegration1D.py </executable>
    <parameters></parameters>
    <metrics>
        <metric type="regex" id="1">
            <regex>^.*Error = ([+-]?\d.+\d|-?\d|[+-]?nan|[+-]?inf)</regex>
            <matches>
                <match>
                    <field id="0">0.0381544</field>
                </match>
            </matches>
        </metric>
    </metrics>
</test>
