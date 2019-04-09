import json

from lxml import etree

XSL = '''<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
    <xsl:output method="text"/>

    <xsl:template match="/collection">
        <xsl:text>{</xsl:text>
            <xsl:apply-templates/>
        <xsl:text>}</xsl:text>
    </xsl:template>

    <xsl:template match="genre">
        <xsl:text>"</xsl:text>
            <xsl:value-of select="@category"/>
        <xsl:text>": [</xsl:text>
        <xsl:for-each select="descendant::movie" >
            <xsl:text>"</xsl:text>
                <xsl:value-of select="@title"/>
            <xsl:text>"</xsl:text>
            <xsl:if test="position() != last()">
                <xsl:text>, </xsl:text>
            </xsl:if>
        </xsl:for-each>
        <xsl:text>]</xsl:text>
        <xsl:if test="following-sibling::*">
            <xsl:text>,
</xsl:text>
        </xsl:if>
    </xsl:template>

    <xsl:template match="text()"/>
</xsl:stylesheet>'''

# load input
dom = etree.parse('movies.xml')
# load XSLT
transform = etree.XSLT(etree.fromstring(XSL))

# apply XSLT on loaded dom
json_text = str(transform(dom))

# json_text contains the data converted to JSON format.
# you can use it with the JSON API. Example:
data = json.loads(json_text)
print(data)