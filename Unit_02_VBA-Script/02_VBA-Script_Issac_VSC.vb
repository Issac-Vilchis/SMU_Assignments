Sub StockDataE()
    Dim ws As Worksheet
    Dim starting_ws As Worksheet
    Set starting_ws = ActiveSheet
    For Each ws In ThisWorkbook.Worksheets
        ws.Activate
    Dim Ticker As String

    Dim Volume As Double
        Volume = 0
    Dim TBR As Long
        TBR = 2
    Dim Year As Double
        Year = Cells(2, 3).Value
    Dim LR As Long
        LR = Cells(Rows.Count, 1).End(xlUp).Row
    Dim LT As Long
        LT = Cells(Rows.Count, 10).End(xlUp).Row

    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Total Stock Volume"
    
    For i = 2 To LR
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        Ticker = Cells(i, 1).Value
        Volume = Volume + Cells(i, 7).Value
        Range("I" & TBR).Value = Ticker
        Range("J" & TBR).Value = Volume
        TBR = TBR + 1
        Year = Cells(i + 1, 3).Value
        Volume = 0
        Else
        Volume = Volume + Cells(i, 7).Value
        End If
    Next i
    For i = 2 To LT
        If Cells(i, 10).Value > GreatestV Then
        GVA = Cells(i, 9).Value
        End If
    Next i
    starting_ws.Activate
    Next ws
End Sub

Sub StockDataM()
    Dim ws As Worksheet
    Dim starting_ws As Worksheet
    Set starting_ws = ActiveSheet
    For Each ws In ThisWorkbook.Worksheets
        ws.Activate
    Dim Ticker As String
    Dim YearCh
        YearCh = 0
    Dim PercentCh
        PercentCh = 0
    Dim Volume As Double
        Volume = 0
    Dim TBR As Long
        TBR = 2
    Dim Year As Double
        Year = Cells(2, 3).Value
    Dim LR As Long
        LR = Cells(Rows.Count, 1).End(xlUp).Row
    Dim LT As Long
        LT = Cells(Rows.Count, 12).End(xlUp).Row

    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Stock Volume"
    
    For i = 2 To LR
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        Ticker = Cells(i, 1).Value
        YearCh = Cells(i, 6).Value - Year
        If Year = 0 Then
            PercentCh = 0
        Else
            PercentCh = YearCh / Year
        End If
        Volume = Volume + Cells(i, 7).Value
        Range("I" & TBR).Value = Ticker
        Range("J" & TBR).Value = YearCh
        If Range("J" & TBR).Value > 0 Then
            Range("J" & TBR).Interior.ColorIndex = 4
        ElseIf Range("J" & TBR).Value < 0 Then
            Range("J" & TBR).Interior.ColorIndex = 3
        End If
        Range("K" & TBR).Value = PercentCh
        Range("K" & TBR).NumberFormat = "0%"
        Range("L" & TBR).Value = Volume
        TBR = TBR + 1
        Year = Cells(i + 1, 3).Value
        PercentCh = 0
        Volume = 0
        Else
        Volume = Volume + Cells(i, 7).Value
        End If
    Next i
    For i = 2 To LT
        If Cells(i, 12).Value > GreatestV Then
        GVA = Cells(i, 9).Value
        End If
    Next i
    starting_ws.Activate
    Next ws
End Sub

Sub StockDataH()
    Dim ws As Worksheet
    Dim starting_ws As Worksheet
    Set starting_ws = ActiveSheet
    For Each ws In ThisWorkbook.Worksheets
        ws.Activate
    Dim Ticker As String
    Dim YearCh
        YearCh = 0
    Dim PercentCh
        PercentCh = 0
    Dim Volume As Double
        Volume = 0
    Dim TBR As Long
        TBR = 2
    Dim Year As Double
        Year = Cells(2, 3).Value
    Dim LR As Long
        LR = Cells(Rows.Count, 1).End(xlUp).Row
    Dim LV As Long
        LV = Cells(Rows.Count, 11).End(xlUp).Row
    Dim LT As Long
        LT = Cells(Rows.Count, 12).End(xlUp).Row
    Dim HighestPc As Double
        HighestPc = 0
    Dim HPA As String
    Dim LowestPc As Double
        LowestPc = 0
    Dim LPA As String
    Dim GreatestVl As Double
        GreatestVl = 0
    Dim GVA As String

    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Stock Volume"
    Cells(2, 15).Value = "Greatest % Increase"
    Cells(3, 15).Value = "Greatest % Decrease"
    Cells(4, 15).Value = "Greatest Total Volume"
    Cells(1, 16).Value = "Ticker"
    Cells(1, 17).Value = "Value"
    
    For i = 2 To LR
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        Ticker = Cells(i, 1).Value
        YearCh = Cells(i, 6).Value - Year
        If Year = 0 Then
            PercentCh = 0
        Else
            PercentCh = YearCh / Year
        End If
        Volume = Volume + Cells(i, 7).Value
        Range("I" & TBR).Value = Ticker
        Range("J" & TBR).Value = YearCh
        If Range("J" & TBR).Value > 0 Then
            Range("J" & TBR).Interior.ColorIndex = 4
        ElseIf Range("J" & TBR).Value < 0 Then
            Range("J" & TBR).Interior.ColorIndex = 3
        End If
        Range("K" & TBR).Value = PercentCh
        Range("K" & TBR).NumberFormat = "0%"
        Range("L" & TBR).Value = Volume
        TBR = TBR + 1
        Year = Cells(i + 1, 3).Value
        PercentCh = 0
        Volume = 0
        Else
        Volume = Volume + Cells(i, 7).Value
        End If
    Next i
    
    For i = 2 To LV
        If Cells(i, 11).Value > HighestPc Then
            HighestPc = Cells(i, 11).Value
            HPA = Cells(i, 9).Value
        End If
        If Cells(i, 11).Value < LowestPc Then
            LowestPc = Cells(i, 11).Value
            LPA = Cells(i, 9).Value
        End If
    Next i
        
    For i = 2 To LT
        If Cells(i, 12).Value > GreatestVl Then
        GreatestVl = Cells(i, 12).Value
        GVA = Cells(i, 9).Value
        End If
    Next i
    
    Cells(2, 17).Value = HighestPc
        Cells(2, 17).NumberFormat = "0%"
    Cells(2, 16).Value = HPA
    Cells(3, 17).Value = LowestPc
        Cells(3, 17).NumberFormat = "0%"
    Cells(3, 16).Value = LPA
    Cells(4, 17).Value = GreatestVl
    Cells(4, 16).Value = GVA
    
    starting_ws.Activate
    Next ws
End Sub