
def insert_newlines(string,every=50):
    lines=[]
    for i in range(0,len(string),every):
        lines.append(string[i:i+every])
    return lines

def format_alignment_linebreak(align1_linebreaks,align2_linebreaks,score,begin,end,seq1_id,seq2_id):
    s=[]
    for line in range(0,len(align1_linebreaks)):
        s.append(seq1_id + ":" + "%s%s\n" %(" "*((max(len(seq1_id),len(seq2_id))+1)-len(seq1_id)),align1_linebreaks[line]))
        s.append("%s%s\n" % (" "*(max(len(seq1_id),len(seq2_id))+2), "|" * (len(align1_linebreaks[line]))))
        s.append(seq2_id + ":" + "%s%s\n" %(" "*((max(len(seq1_id),len(seq2_id))+1)-len(seq2_id)),align2_linebreaks[line]))
        s.append('\n')
    s.append("  Score=  %g\n" % score)
    s.append("  Begin=  %g\n" % begin)
    s.append("  End  =  %g\n" % end)
    s.append("  Length= %g\n" % (end-begin))
    return ''.join(s)
