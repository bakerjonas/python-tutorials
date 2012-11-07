import Tkinter

class Heatmap:
    '''
    Heatmap visualizer
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass

    def loadPclFile(self, filename, logger=None):
        '''
        Load data from a PCL file.

        @param filename: file to load
        @param logger: optional logger
        @return (geneIds, sampleIds, expValues), where geneIds is a list of integers,
        sampleIds is a list of strings, and expValues has a list of expression values
        for each gene in the geneIds list
        '''
        fp = open(filename)

        # parse header line
        line = fp.readline()
        if line == '':
            if logger != None:
                logger.warn('Invalid file, no header line: %s' % (filename))
            return None
        line.strip()
        sampleIds = line.split('\t')[3:] # first 3 columns are gene id, gene name, and gweight

        # Ignore eweight line
        line = fp.readline()
        if line == '':
            if logger != None:
                logger.warn('Invalid file, no header line: %s' % (filename))

        # Parse expression values
        geneIds = []   # same order as in file
        expValues = [] # same order as geneIds
        while True:
            line = fp.readline()
            if line == '':
                break

            line = line.strip()
            cols = line.split('\t')
            geneIds.append(cols[0])
            exps = []
            for c in cols[3:]:
                exps.append(float(c))
            expValues.append(exps)

        fp.close()
        return (geneIds, sampleIds, expValues)

    def loadMappingFile(self, filename, logger=None):
        '''
        Load gene ID to gene name mappings from a file

        @param filename: file to load
        @param logger: optional logger
        @return dict with gene ID to name mappings
        '''
        fp = open(filename)

        geneId2Name = {} # Gene ID to name mappings

        while True:
            line = fp.readline()
            if line == '':
                break

            line = line.strip()
            name, gid = line.split('\t')
            if gid in geneId2Name:
                # Check if the new mappnig is 'better'
                oldName = geneId2Name[gid]
                if (oldName.find('_at') != -1 or oldName.isdigit()) and (name.find('_at') == -1 and not name.isdigit()):
                    geneId2Name[gid] = name
            else:
                geneId2Name[gid] = name

        fp.close()
        return geneId2Name

    def convertFoldToHexColor(self, val, cutoff=2.0):
        '''
        Convert expression value to a RGB color code

        @param val: expression value
        @param cutoff: optional cutoff value. Expression values above the cutoff
        are set to the maximum color value.
        @return: a string with hexadesimal RGB color values for the expression value
        '''
        color = "#"
        if val > 0:
            # Red
            if val < cutoff:
                amount = int(255 * (val / cutoff))
                if amount < 16:
                    color += "0"
                color += hex(amount)[2:]
            else:
                color += "FF"
                # Green
            color += "00"
            # Blue
            color += "00"
        else:
        # Red
            color += "00"
            # Green
            if val > (-1 * cutoff):
                amount = int(255 * ((-1 * val) / cutoff))
                if amount < 16:
                    color += "0"
                color += hex(amount)[2:]
            else:
                color += "FF"
                # Blue
            color += "00"

        return color

    def createHeatmap(self, root, geneIds, sampleIds, expValues, geneId2Name, rowHeight=20, canvasWidth=500, labelWidth=50):
        '''
        Create a Tkinter canvas with a heatmap visualization

        @param root: Tkinter top level window
        @param geneIds: list with gene IDs
        @param sampleIds: list with sample IDs
        @param expValues: list of list with expression values
        @param geneId2Name: dict with gene ID to gene name mappings
        @param rowHeight: optional height for a row in the heatmap
        @param canvasWidth: optional width for the canvas
        @param labelWidth: optional width for gene name labels
        '''

        # The canvas height depends on the number of genes in the dataset
        canvasHeight = (len(geneIds) + 1) * rowHeight
        self.canvasHeight = canvasHeight
        # The column width depends on the number of samples in the dataset
        columnWidth = (canvasWidth - labelWidth)  / len(sampleIds)
        self.columnWidth = columnWidth

        # Create a frame with a vertically scrollable canvas
        frame = Tkinter.Frame(root, width=columnWidth, height=canvasHeight)
        frame.place(x=0, y=0)
        frame.pack(fill=Tkinter.BOTH, expand=1)
        canvas = Tkinter.Canvas(frame, width=columnWidth, height=canvasHeight, scrollregion=(0,0,columnWidth,canvasHeight))
        vbar = Tkinter.Scrollbar(frame,orient=Tkinter.VERTICAL)
        vbar.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)
        vbar.config(command=canvas.yview)
        canvas.place(x=0, y=0)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(fill=Tkinter.BOTH, expand=True)

        # Paint gene IDs
        rowIDs = []
        for i in range(len(geneIds)):
            name = geneIds[i]
            if name in geneId2Name:
                name = geneId2Name[name]
            # TODO: create a label with the gene name

        # Paint column IDs
        for i in range(len(sampleIds)):
            # TODO: crete a label with the sample ID

        cutoff = 2.0
        # Paint expression values
        for i in range(len(geneIds)):
            avg = 0.0
            count = 0.0
            for e in expValues[i]:
                avg = avg + e
                count = count + 1
            if count > 0:
                avg = avg / count

            for j in range(len(sampleIds)):
                x = (j * columnWidth) + labelWidth
                y = (i * rowHeight) + rowHeight
                val = expValues[i][j]
                color = self.convertFoldToHexColor(val - avg, cutoff)
                # TODO: create rectangle for expression value

        return canvas

if __name__ == '__main__':
    import sys

    assert(len(sys.argv) == 3), 'Usage: python %s pclFilename mappingFilename' % (sys.argv[0])
    pclFilename = sys.argv[1]
    mappingFilename = sys.argv[2]

    heatmap = Heatmap()
    geneIds, sampleIds, expValues = heatmap.loadPclFile(pclFilename)
    geneId2Name = heatmap.loadMappingFile(mappingFilename)
    root = Tkinter.Tk()
    # Set initial window position and size
    root.geometry("525x525+100+100")
    heatmap.createHeatmap(root, geneIds, sampleIds, expValues, geneId2Name)
    # Enter GUI root
    root.mainloop()
