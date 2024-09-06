# Generated from CSP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSPParser import CSPParser
else:
    from CSPParser import CSPParser

# This class defines a complete listener for a parse tree produced by CSPParser.
class CSPListener(ParseTreeListener):

    # Enter a parse tree produced by CSPParser#cspFile.
    def enterCspFile(self, ctx:CSPParser.CspFileContext):
        pass

    # Exit a parse tree produced by CSPParser#cspFile.
    def exitCspFile(self, ctx:CSPParser.CspFileContext):
        pass


    # Enter a parse tree produced by CSPParser#processDefinition.
    def enterProcessDefinition(self, ctx:CSPParser.ProcessDefinitionContext):
        pass

    # Exit a parse tree produced by CSPParser#processDefinition.
    def exitProcessDefinition(self, ctx:CSPParser.ProcessDefinitionContext):
        pass


    # Enter a parse tree produced by CSPParser#channelDefinition.
    def enterChannelDefinition(self, ctx:CSPParser.ChannelDefinitionContext):
        pass

    # Exit a parse tree produced by CSPParser#channelDefinition.
    def exitChannelDefinition(self, ctx:CSPParser.ChannelDefinitionContext):
        pass


    # Enter a parse tree produced by CSPParser#parameters.
    def enterParameters(self, ctx:CSPParser.ParametersContext):
        pass

    # Exit a parse tree produced by CSPParser#parameters.
    def exitParameters(self, ctx:CSPParser.ParametersContext):
        pass


    # Enter a parse tree produced by CSPParser#expression.
    def enterExpression(self, ctx:CSPParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#expression.
    def exitExpression(self, ctx:CSPParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#prefixExpression.
    def enterPrefixExpression(self, ctx:CSPParser.PrefixExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#prefixExpression.
    def exitPrefixExpression(self, ctx:CSPParser.PrefixExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#baseExpression.
    def enterBaseExpression(self, ctx:CSPParser.BaseExpressionContext):
        pass

    # Exit a parse tree produced by CSPParser#baseExpression.
    def exitBaseExpression(self, ctx:CSPParser.BaseExpressionContext):
        pass


    # Enter a parse tree produced by CSPParser#eventList.
    def enterEventList(self, ctx:CSPParser.EventListContext):
        pass

    # Exit a parse tree produced by CSPParser#eventList.
    def exitEventList(self, ctx:CSPParser.EventListContext):
        pass


    # Enter a parse tree produced by CSPParser#event.
    def enterEvent(self, ctx:CSPParser.EventContext):
        pass

    # Exit a parse tree produced by CSPParser#event.
    def exitEvent(self, ctx:CSPParser.EventContext):
        pass



del CSPParser