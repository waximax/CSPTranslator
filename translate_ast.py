from antlr4 import *
from CSPParser import CSPParser
from CSPLexer import CSPLexer
from CSPVisitor import CSPVisitor

class CSPToASTVisitor(CSPVisitor):
    def __init__(self):
        self.result = []  # 用于存储翻译结果

    def visitChannelDefinition(self, ctx: CSPParser.ChannelDefinitionContext):
        channel_name = ctx.ID(0).getText()
        range_values = ctx.INT(0).getText()
        if ctx.INT(1):
            range_values += f"..{ctx.INT(1).getText()}"
        self.result.append(f"Channel {channel_name} declared with range {{{range_values}}}.")
        return None

    def visitProcessDefinition(self, ctx: CSPParser.ProcessDefinitionContext):
        process_name = ctx.ID().getText()
        self.result.append(f"Process {process_name} is defined.")
        expression = ctx.expression()
        return self.visit(expression)

    def visitExpression(self, ctx: CSPParser.ExpressionContext):
        if ctx.getChildCount() == 3:
            operator = ctx.getChild(1).getText()
            if operator == '[]':
                process1 = self.visit(ctx.getChild(0))
                process2 = self.visit(ctx.getChild(2))
                result = (f"This choice is external, meaning it depends on how the process interacts with its environment. "
                          f"The choice between {process1} and {process2} is determined by the actual events that occur. "
                          f"This choice does not involve synchronization between {process1} and {process2}; "
                          f"rather, it is determined based on the behavior of the external environment.")
                self.result.append(result)
                return result
            elif operator == '&':
                condition = ctx.getChild(0).getText()
                guarded_process = self.visit(ctx.getChild(2))
                if guarded_process is None:
                    guarded_process = "STOP"
                if condition == "true":
                    result = f"If the condition is true, the process behaves as {guarded_process}."
                else:
                    result = f"If the condition is false, the process behaves as {guarded_process}."
                self.result.append(result)
                return result
            elif operator == '|||':
                process1 = self.visit(ctx.getChild(0))
                process2 = self.visit(ctx.getChild(2))
                result = (f"The processes {process1} and {process2} are interleaved, meaning they run in parallel "
                          f"without any synchronization. This is equivalent to {process1} [| {{}} |] {process2}.")
                self.result.append(result)
                return result
            elif operator == ';':
                process1 = self.visit(ctx.getChild(0))
                process2 = self.visit(ctx.getChild(2))
                result = (f"The process {process1} runs first. Once it terminates (turns into SKIP), "
                          f"the process {process2} will begin execution.")
                self.result.append(result)
                return result
        elif ctx.getChildCount() == 11:
            process1 = self.visit(ctx.getChild(0))
            process2 = self.visit(ctx.getChild(10))
            events1 = "{" + ctx.getChild(3).getText() + "}"
            events2 = "{" + ctx.getChild(7).getText() + "}"
            result = (f"Process {process1} and Process {process2} must synchronize on the intersection "
                      f"of the event sets {events1} and {events2}. "
                      f"If there is no intersection between {events1} and {events2}, then {process1} "
                      f"and {process2} can execute in parallel without requiring synchronization.")
            self.result.append(result)
            return result
        elif ctx.getChildCount() == 7:
            process1 = self.visit(ctx.getChild(0))
            process2 = self.visit(ctx.getChild(6))
            events = "{" + ctx.getChild(3).getText() + "}"
            result = (f"The processes {process1} and {process2} must synchronize on these events, either {events}. "
                      f"This means that when either {process1} or {process2} performs these events, "
                      f"the other process must also perform the same event to ensure coordination between the two processes.")
            self.result.append(result)
            return result
        return self.visitChildren(ctx)

    def visitPrefixExpression(self, ctx: CSPParser.PrefixExpressionContext):
        event = ctx.event().getText()
        process = self.visit(ctx.expression())
        if process is None:
            process = "STOP"
        event_description = f"{event} is an event that represents sending the value {event.split('.')[1]} through the channel {event.split('.')[0]}."
        result = f"{event_description} Followed by a transition to the {process} state."
        self.result.append(result)
        return process

    def visitBaseExpression(self, ctx: CSPParser.BaseExpressionContext):
        if ctx.STOP_RULE():
            return "STOP"
        elif ctx.SKIP_RULE():
            return "SKIP"
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None

    def get_translation(self):
        return "\n".join(self.result)

def translate_csp_code(csp_code):
    print(f"Received CSP code:\n{csp_code}")  # 输出接收到的 CSP 代码，用于调试
    input_stream = InputStream(csp_code)
    lexer = CSPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSPParser(stream)
    tree = parser.cspFile()

    visitor = CSPToASTVisitor()
    visitor.visit(tree)
    translation_result = visitor.get_translation()
    print(f"Translation result:\n{translation_result}")  # 输出翻译结果，用于调试
    return translation_result
