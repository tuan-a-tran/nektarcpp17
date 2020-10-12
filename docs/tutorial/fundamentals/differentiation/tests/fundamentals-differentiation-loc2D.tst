<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description> LocDifferentiation2D tutorial  </description>
    <executable> LocDifferentiation2D </executable>
    <parameters> </parameters>
    <metrics>
        <metric type="regex" id="1">
            <regex>^.*Error = ([+-]?\d.+\d|-?\d|[+-]?nan|[+-]?inf)</regex>
            <matches>
                <match>
                    <field id="0">0.0346594</field>
                </match>
            </matches>
        </metric>
    </metrics>
</test>
