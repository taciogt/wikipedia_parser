# -*- coding: utf8 -*-

__author__ = 'tacio'


import unittest
import wiki_formatter


class TestCharacterFormatting(unittest.TestCase):

    def test_extract_text(self):
        text = '''<page>
                    <title>Astronomia</title>
                    <ns>0</ns>
                    <id>220</id>
                    <revision>
                      <id>38377833</id>
                      <parentid>38377778</parentid>
                      <timestamp>2014-03-11T23:10:33Z</timestamp>
                      <contributor>
                        <username>Marcos Elias de Oliveira Júnior</username>
                        <id>630796</id>
                      </contributor>
                      <comment>Desfeita a edição 38377778 de [[Special:Contribs/186.221.145.28|186.221.145.28]]</comment>
                      <text xml:space="preserve">Conteúdo real do artigo</text>
                      <sha1>36th0eaaduq90zljs8ryv2g2ed5c47o</sha1>
                      <model>wikitext</model>
                      <format>text/x-wiki</format>
                    </revision>
                  </page>'''
        formatted_text = "Conteúdo real do artigo"
        self.assertEqual(formatted_text, wiki_formatter.format_text(text))

        text = '''<page>
                    <title>Astronomia</title>
                    <revision>
                      <text>Conteúdo real</text>
                    </revision>
                  </page>'''
        formatted_text = "Conteúdo real"
        self.assertEqual(formatted_text, wiki_formatter.format_text(text))