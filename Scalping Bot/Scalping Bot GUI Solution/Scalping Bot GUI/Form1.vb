' Drew Schmidt
' Scalping Bot GUI
' 5/18/21

Option Explicit On
Option Strict On
Option Infer Off

Public Class frmScalper

    Private Sub btnStart_Click(sender As Object, e As EventArgs) Handles btnStart.Click

        Dim filePath As String = "variables.txt"
        Dim lines() As String = System.IO.File.ReadAllLines(filePath)
        Dim file_path3080fe As String = txtFilePath1.Text & "\python.exe" & " " & txtFilePath0.Text & "\Scripts\3080\BB3080FE.py"
        Dim file_path3080evga As String = txtFilePath1.Text & "\python.exe" & " " & txtFilePath0.Text & "\Scripts\3080\BB3080EVGA.py"

        lines(1) = txtFirst.Text()
        lines(2) = txtLast.Text()
        lines(3) = txtEmail.Text()
        lines(4) = txtPassword.Text()
        lines(5) = txtPhone.Text()
        lines(6) = txtStreet.Text()
        lines(7) = txtCity.Text()
        lines(8) = txtState.Text()
        lines(9) = txtZipcode.Text()
        lines(10) = txtCardNumber.Text()
        lines(11) = txtExpMonth.Text()
        lines(12) = txtExpYear.Text()
        lines(13) = txtCIV.Text()

        System.IO.File.WriteAllLines(filePath, lines)



    End Sub

    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click

        Me.Close()
    End Sub

End Class
