<?xml version="1.0" encoding="utf-8" ?>
<test>
    <description> StdDifferentiation1D tutorial  </description>
    <executable python="true"> StdDifferentiation1D.py </executable>
    <parameters> </parameters>
    <metrics>
        <metric type="regex" id="1">
            <regex>^.*Error = ([+-]?\d.+\d|-?\d|[+-]?nan|[+-]?inf)</regex>
            <matches>
                <match>
                    <field id="0">1.49647</field>
                </match>
            </matches>
        </metric>
    </metrics>
</test>
