# Array f�r alle pingbaren Ger�te            
$alleOnlineGeraete = @()            
            
# Array f�r alle NICHT pingbaren Ger�te            
$alleOfflineGeraete = @()            
            
# Ganzes Netzwerksegment von 1 bis 255            
$alleIPs = (1..255)            
            
# Auswahl der Netzwerkkarte bzw. IP Adresse die f�r den Ping verwendet werden soll            
$gewaehlteIP = Get-NetIPAddress | where {$_.IPAddress -like "192.168.*" -or $_.IPAddress -like "10.*" `
-or $_.IPAddress -like "172.16.*"} | Sort-Object InterfaceIndex | select IPAddress |  Out-GridView -Title "W�hle die Netzwerkkarte" -PassThru            
            
# Teilen der gew�hlten IP Adresse, damit nur die ersten 3 Oktetts verwendet werden            
$splitIP = $gewaehlteIP.IPAddress.Split(".")[0..2] -join "."            
            
# Am Ende der 3 Oktetts noch ein Punkt (.) anh�ngen            
$splitIP += "."            
            
# Testen der Verbindung aller IPs im Bereich $alleIPs            
foreach ($ip in $alleIPs)            
{            
    # Generieren der IP Adressen bzw. des letzten Oktetts und zusammensetzen            
    $testIP = $splitIP + $ip            
            
    # Testen der Verbindung mit 2 Pings (-Count 2) mit R�ckgabe $true oder $false (-Quiet)            
    if (Test-Connection -Count 1 -BufferSize 2 -Quiet $testIP)             
        {            
            # Schreiben bei Erfolg            
            Write-Output "$testIP Online"            
                    
            # Array erg�nzen mit dem Online Ger�t            
            $alleOnlineGeraete += $testIP            
        }             
    else             
        {            
            # Schreiben bei Misserfolg            
            Write-Output "$testIP Offline"            
                        
            # Array erg�nzen mit dem Offline Ger�t            
            $alleOfflineGeraete += $testIP            
        }            
}            
            
# Ausgabe der Online Ger�te            
"Online sind:"            
$alleOnlineGeraete             
            
# Ausgabe der Offline Ger�te            
"Offline sind:"            
$alleOfflineGeraete

Read-Host -Prompt "Bitte eine beliebige Taste zum Beenden dr�cken ..."