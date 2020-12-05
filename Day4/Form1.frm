VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   3015
   ClientLeft      =   120
   ClientTop       =   465
   ClientWidth     =   4560
   LinkTopic       =   "Form1"
   ScaleHeight     =   3015
   ScaleWidth      =   4560
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton Command1 
      Caption         =   "Command1"
      Height          =   495
      Left            =   360
      TabIndex        =   0
      Top             =   480
      Width           =   1335
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim fields As Variant
Private Sub Command1_Click()
    Dim MyLine As String
    Dim line As String
    
    fields = Array("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    counting = 0
    counting2 = 0
    Open "C:\Users\Erika\Documents\AdventOfCode\Day4\input.txt" For Input As #1
        Do While Not EOF(1)
            Line Input #1, MyLine
            If (MyLine = "") Then
                If (CountFields(line) = True) Then
                    counting = counting + 1
                End If
                line = ""
            Else
                If line = "" Then
                    line = MyLine
                Else
                    line = line + " " + MyLine
                End If
            End If
        Loop
        If (CountFields(line) = True) Then
            counting = counting + 1
        End If
    Close #1
    MsgBox counting
End Sub

Private Function CountFields(line As String) As Boolean
    Dim splitLine As Variant
    Dim countedFields As Integer
    Dim returned As Boolean
    Dim valid As Integer
    countedFields = 0
    splitLine = Split(line, " ")
    For index = 0 To UBound(splitLine)
        Dim fieldValue() As String
        fieldValue = Split(splitLine(index), ":")
        
        If Not (fieldValue(0) = "cid") Then
            If (Validate(fieldValue(0), fieldValue(1)) = True) Then
                valid = valid + 1
            End If
        End If
        For i = 0 To UBound(fields)
            If fields(i) = fieldValue(0) Then
                countedFields = countedFields + 1
                Exit For
            End If
        Next
    Next
    If countedFields = 7 And valid = 7 Then
        CountFields = True
    Else
        CountFields = False
    End If
End Function

Private Function Validate(field As String, value As String) As Boolean
    Select Case (field)
        Case "byr"
            Validate = ValidateLength(value, 4) And ValidateInterval(CInt(value), 1920, 2002)
        Case "iyr"
            Validate = ValidateLength(value, 4) And ValidateInterval(CInt(value), 2010, 2020)
        Case "eyr"
            Validate = ValidateLength(value, 4) And ValidateInterval(CInt(value), 2020, 2030)
        Case "hgt"
            Validate = ValidateHeight(value)
        Case "hcl"
            Validate = ValidateHair(value)
        Case "ecl"
            Validate = ValidateEyeColor(value)
        Case "pid"
            Validate = ValidateLength(value, 9)
        Case Else
            Validate = False
    End Select
End Function

Private Function ValidateHeight(value As String) As Boolean
    Dim posCm As Integer
    Dim posIn As Integer
    posCm = InStr(1, value, "cm")
    posIn = InStr(1, value, "in")
    If (posCm > 0) Then
        posCm = Mid(value, 1, Len(value) - 2)
        If (ValidateInterval(posCm, 150, 193) = True) Then
            ValidateHeight = True
            Exit Function
        End If
    End If
    If (posIn > 0) Then
        posIn = Mid(value, 1, Len(value) - 2)
        If (ValidateInterval(posIn, 59, 76) = True) Then
            ValidateHeight = True
            Exit Function
        End If
    End If
    ValidateHeight = False
End Function

Private Function ValidateHair(value As String) As Boolean
    Dim hexa As Variant
    Dim valueArray As Variant
    valueArray = StringToChar(value)
    hexa = Array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f")
    If (Len(value) = 7 And Left(value, 1) = "#") Then
        For i = 1 To UBound(valueArray)
            ValidateHair = False
            For j = 0 To UBound(hexa)
                If hexa(j) = valueArray(i) Then
                    ValidateHair = True
                    Exit For
                End If
            Next
            If ValidateHair = False Then
                Exit Function
            End If
        Next
    End If
End Function

Private Function StringToChar(text As String) As String()
    Dim myCharArray() As String
    Dim i As Integer
    ReDim myCharArray(Len(text) - 1)
    
    For i = 1 To Len(text)
        myCharArray(i - 1) = Mid(text, i, 1)
    Next i
    StringToChar = myCharArray
End Function

Private Function ValidateLength(value As String, length) As Boolean
    If (Len(value) = length) Then
        ValidateLength = True
    Else
        ValidateLength = False
    End If
End Function

Private Function ValidateInterval(value As Integer, min As Integer, max As Integer) As Boolean
    If (value >= min And value <= max) Then
        ValidateInterval = True
    Else
        ValidateInterval = False
    End If
End Function

Private Function ValidateEyeColor(value As String) As Boolean
    Dim eyeColors As Variant
    eyeColors = Array("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    For i = 0 To UBound(eyeColors)
        If eyeColors(i) = value Then
            ValidateEyeColor = True
            Exit Function
        End If
    Next
    ValidateEyeColor = False
End Function
