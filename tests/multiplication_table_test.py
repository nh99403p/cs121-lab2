import re
import multiplication_table

def test_multiplication_table(capsys):
    output = r"\s*.*1\s+2\s+3\s+4\s+5\s+6\s+7\s+8\s+9\s+10\s+\n\s*.*2\s+4\s+6\s+8\s+10\s+12\s+14\s+16\s+18\s+20\s+\n\s*.*3\s+6\s+9\s+12\s+15\s+18\s+21\s+24\s+27\s+30\s+\n\s*.*4\s+8\s+12\s+16\s+20\s+24\s+28\s+32\s+36\s+40\s+\n\s*.*5\s+10\s+15\s+20\s+25\s+30\s+35\s+40\s+45\s+50\s+\n\s*.*6\s+12\s+18\s+24\s+30\s+36\s+42\s+48\s+54\s+60\s+\n\s*.*7\s+14\s+21\s+28\s+35\s+42\s+49\s+56\s+63\s+70\s+\n\s*.*8\s+16\s+24\s+32\s+40\s+48\s+56\s+64\s+72\s+80\s+\n\s*.*9\s+18\s+27\s+36\s+45\s+54\s+63\s+72\s+81\s+90\s+\n\s*.*10\s+20\s+30\s+40\s+50\s+60\s+70\s+80\s+90\s+100\s+\n"
    multiplication_table.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out)