EXPR_GRAMMAR = {
    "<Document>":
        ["<Definition>","<Definition>\n<Document>"],
    "<Definition>":
        ["<OperationDefinition>","<FragmentDefinition>"],
    "<OperationDefinition>":
        ["<OperationType> <NameOPT> <VariableDefinitionsOPT> <DirectivesOPT> <SelectionSet>","<SelectionSet>"],
    "<NameOPT>":
        ["<Name>",""],
    "<VariableDefinitionsOPT>":
        ["<VariableDefinitions>",""],
    "<DirectivesOPT>":
        ["<Directives>",""],
    "<OperationType>":
        ["query","mutation"],
    "<SelectionSet>":
        ["{ <Selections> }"],
    "<Selections>":
        ["<Selection>","<Selection>\n<Selections>"],
    "<Selection>":
        ["<Field>","<FragmentSpread>","<InlineFragment>"],
    "<Field>":
        ["<AliasOPT> <Name> <ArgumentsOPT> <DirectivesOPT> <SelectionSetOPT>"],
    "<AliasOPT>":
        ["<Alias>",""],
    "<ArgumentsOPT>":
        ["<Arguments>",""],
    "<SelectionSetOPT>":
        ["<SelectionSet>",""],
    "<Alias>":
        ["<Name> : "],
    "<Arguments>":
        ["( <ArgumentList> )"],
    "<ArgumentList>":
        ["<Argument>","<Argument>, <ArgumentList>"],
    
    "<Argument>":
        ["<Name> : <Value>"],
    "<FragmentSpread>":
        ["... <FragmentName> <DirectivesOPT>"],
    "<InlineFragment>":
        ["... <TypeConditionOPT> <DirectivesOPT> <SelectionSet>"],
    "<TypeConditionOPT>":
        ["<TypeCondition>",""],
    "<FragmentDefinition>":
        ["fragment <FragmentName> <TypeCondition> <DirectivesOPT> <SelectionSet>"],
    "<FragmentName>":
        ["<Name>"],
    "<TypeCondition>":
        ["on <NamedType>"],
    "<Value>":
        ["<Variable>","<IntValue>","<FloatValue>","<StringValue>","<BooleanValue>","<EnumValue>","<ListValue>","<ObjectValue>"],
    "<Value_Const>":
        ["<IntValue>","<FloatValue>","<StringValue>","<BooleanValue>","<EnumValue>","<ListValue_Const>","<ObjectValue_Const>"],
    "<BooleanValue>":
        ["true","false"],
    "<EnumValue>":
        ["<Name>"],
    "<ListValue>":
        ["[]","[ <Values> ]"],
    "<Values>":
        ["<Value>","<Value>, <Values>"],
    "<ListValue_Const>":
        ["[]","[ <Values_Const> ]"],
    "<Values_Const>":
        ["<Value_Const>","<Value_Const>, <Values_Const>"],
    "<ObjectValue>":
        ["{}","{ <ObjectFields> }"],
    "<ObjectFields>":
        ["<ObjectField>","<ObjectField>, <ObjectFields>"],
    "<ObjectValue_Const>":
        ["{}","{ <ObjectFields_Const> }"],
    "<ObjectFields_Const>":
        ["<ObjectField_Const>","<ObjectField_Const>, <ObjectFields_Const>"],
    "<ObjectField>":
        ["<Name> : <Value>"],
    "<ObjectField_Const>":
        ["<Name> : <Value_Const>"],
    "<VariableDefinitions>":
        ["( <VariableDefinitionList> )"],
    "<VariableDefinitionList>":
        ["<VariableDefinition>","<VariableDefinition>, <VariableDefinitionList>"],
    "<VariableDefinition>":
        ["<Variable> : <Type> <DefaultValueOPT>"],
    "<DefaultValueOPT>":
        ["","<DefaultValue>"],
    "<Variable>":
        ["$<Name>"],
    "<DefaultValue>":
        ["= <Value_Const>"],
    "<Type>":
        ["<NamedType>","<ListType>","<NonNullType>"],
    "<NamedType>":
        ["<Name>"],
    "<ListType>":
        ["[ <Type> ]"],
    "<NonNullType>":
        ["<NamedType> !", "<ListType> !"],
    "<Directives>":
        ["<Directive>", "<Directive> <Directives>"],
    "<Directive>":
        ["@ <Name> <ArgumentsOPT>"],


    "<Name>":
        ["<NameStart><NameContinuesOPT>"],
    "<NameStart>":
        ["<Letter>","_"],
    "<NameContinuesOPT>":
        ["","<NameContinues>"],
    "<NameContinues>":
        ["<NameContinue>","<NameContinue><NameContinues>"],
    "<NameContinue>":
        ["<Letter>","<Digit>","_"],
    "<Letter>":
        ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    "<Digit>":
        ["1","2","3","4","5","6","7","8","9","0"],
    "<IntValue>":
        ["<IntegerPart>"],
    "<IntegerPart>":
        ["<NegativeSignOPT>0","<NegativeSignOPT><NonZeroDigit><DigitsOPT>"],
    "<NegativeSignOPT>":
        ["","<NegativeSign>"],
    "<NegativeSign>":
        ["-"],
    "<NonZeroDigit>":
        ["1","2","3","4","5","6","7","8","9"],
    "<DigitsOPT>":
        ["","<Digits>"],
    "<Digits>":
        ["<Digit>","<Digit><Digits>"],
    "<FloatValue>":
        ["<IntegerPart><FractionalPart><ExponentPart>","<IntegerPart><FractionalPart>","<IntegerPart><ExponentPart>"],
    "<FractionalPart>":
        [".<Digits>"],
    "<ExponentPart>":
        ["<ExponentIndicator><SignOPT><Digits>"],
    "<ExponentIndicator>":
        ["e","E"],
    "<SignOPT>":
        ["","<Sign>"],
    "<Sign>":
        ["+","-"],
    "<StringValue>":
        ["\"\"","\"<StringCharacters>\""],
    "<StringCharacters>":
        ["<StringCharacter>","<StringCharacter><StringCharacters>"],
    "<StringCharacter>":
        ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
        "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "1","2","3","4","5","6","7","8","9","0",
        " ","~","!","@","#","$","%","^","&","*","(",")","_","+","=","{","}","[","]","|",":",";","<",">","?",",","."]
}
