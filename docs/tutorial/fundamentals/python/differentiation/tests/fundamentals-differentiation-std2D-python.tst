<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description> StdDifferentiation2D tutorial  </description>
    <executable python="true"> StdDifferentiation2D.py </executable>
    <parameters> </parameters>
    <metrics>
        <metric type="regex" id="1">
            <regex>^.*Error = ([+-]?\d.+\d|-?\d|[+-]?nan|[+-]?inf)</regex>
            <matches>
                <match>
                    <field id="0">7.19196</field>
                </match>
            </matches>
        </metric>
    </metrics>
</test>
