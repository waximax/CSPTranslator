# Generated from CSP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CSPParser import CSPParser
else:
    from CSPParser import CSPParser

# This class defines a complete generic visitor for a parse tree produced by CSPParser.

class CSPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSPParser#cspFile.
    def visitCspFile(self, ctx:CSPParser.CspFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#processDefinition.
    def visitProcessDefinition(self, ctx:CSPParser.ProcessDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#channelDefinition.
    def visitChannelDefinition(self, ctx:CSPParser.ChannelDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#parameters.
    def visitParameters(self, ctx:CSPParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#expression.
    def visitExpression(self, ctx:CSPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#prefixExpression.
    def visitPrefixExpression(self, ctx:CSPParser.PrefixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#baseExpression.
    def visitBaseExpression(self, ctx:CSPParser.BaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#eventList.
    def visitEventList(self, ctx:CSPParser.EventListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSPParser#event.
    def visitEvent(self, ctx:CSPParser.EventContext):
        return self.visitChildren(ctx)



del CSPParser