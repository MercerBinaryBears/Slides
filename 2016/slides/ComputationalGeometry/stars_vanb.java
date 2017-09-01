
import java.io.*;
import java.util.*;
import java.awt.geom.*;

/**
 * Solution to Star Simulations
 * 
 * The constraint that the stars are sparse, and that there will not be more
 * than 100,000 matching pairs, gives us a neat solution. We'll put all
 * of the stars into kxkxk bins. Then, we only need to check within a bin
 * and in adjacent bins. The sparseness guarantee makes sure that there won't
 * be too many in any bin, and so we won't run into Time Limit Exceeded.
 * 
 * @author vanb
 */
public class stars_vanb
{
    public Scanner sc;
    public PrintStream ps;
    
    /**
     * A Star.
     * 
     * @author vanb
     */
    public class Star
    {
        // Position
        public long x, y, z;
        
        /**
         * Create a Star
         * 
         * @param x X coordinate
         * @param y Y coordinate
         * @param z Z coordinate
         */
        public Star( long x, long y, long z )
        {
            this.x=x; this.y=y; this.z=z;
        }
        
        /**
         * Distance Squared to another star.
         * We'll use squared distance to keep things in integers.
         * 
         * @param s Another star
         * @return Distance squared form this star to s
         */
        public long d2( Star s )
        {
            long dx = x-s.x;
            long dy = y-s.y;
            long dz = z-s.z;
                        
            return dx*dx + dy*dy + dz*dz; 
        }
    }
    
    // Structure for the bins
    public HashMap<String,List<Star>> bins = new HashMap<String,List<Star>>();
    
    // These define the 13 'adjacent' bins to a current bin.
    // Note that if we check the bin at (x+1,y,z), then checking the bin at (x-1,y,z)
    // is redundant. We would have checked those pairings when we handled bin (x-1,y,z)
    public int dx[] = {  1,  0,  0,  1,  1,  0,  1,  1,  1,  0,  1,  1,  1  };
    public int dy[] = {  0,  1,  0,  1,  0,  1,  1, -1,  0,  1,  1, -1, -1  };
    public int dz[] = {  0,  0,  1,  0,  1,  1,  1,  0, -1, -1, -1,  1, -1  };
        
    /**
     * Figure out what bin to put an integer in.
     * 
     * @param i Integer
     * @param k Bin size
     * @return Ordinal index of a bin
     */
    public static String bin( long i, long k )
    {
        long b = i<0 ? ((i+1)/k-1) : i/k;
        return ""+b;
    }
    /**
     * Driver.
     * @throws Exception
     */
    public void doit() throws Exception
    {
        sc = new Scanner( System.in ); //new File( "stars.judge" ) );
        ps = System.out; //new PrintStream( new FileOutputStream( "stars.solution" ) );

        for(;;)
        {
            int n = sc.nextInt();
            long k = sc.nextLong();
            if( n==0 ) break;
            
            bins.clear();
            for( int i=0; i<n; i++ )
            {
                long x = sc.nextLong();
                long y = sc.nextLong();
                long z = sc.nextLong();
                
                // Here's the bin to put this star into
                String key = bin(x,k) + ":" + bin(y,k) + ":" + bin(z,k);
                List<Star> stars = bins.get( key );
                if( stars==null )
                {
                    // If it doesn't exist yet, create it.
                    stars = new LinkedList<Star>();
                    bins.put( key, stars );
                }
                stars.add( new Star( x, y, z ) );
            }
            
            // Remember, we're comparing distance squared.
            long kk = k*k;
            
            int count = 0;
            
            // Go through all of the bins
            String keys[] = (String[])bins.keySet().toArray( new String[bins.keySet().size()] );
            for( String key : keys )
            {
                // Get this bin
                List<Star> bin = bins.get( key );
                
                // Get all of the stars local to this bin
                Star local[] = (Star[])bin.toArray( new Star[bin.size()] );
                
                // Compare the local stars to each other
                for( int i=0; i<local.length; i++ ) for( int j=i+1; j<local.length; j++ )
                {
                    if( local[i].d2( local[j] ) < kk ) ++count;
                }
                
                // Get the indices of this bin
                String tokens[] = key.split( ":" );
                int kx = Integer.parseInt( tokens[0] );
                int ky = Integer.parseInt( tokens[1] );
                int kz = Integer.parseInt( tokens[2] );
                
                // Go through all adjacent bins
                for( int i=0; i<dx.length; i++ )
                {
                    // Get the adjacent bin, if it exists
                    String newkey = "" + (kx+dx[i]) + ":" + (ky+dy[i]) + ":" + (kz+dz[i]);
                    List<Star> newbin = bins.get( newkey );
                    if( newbin!=null )
                    {
                        // Compare all of the stars in this bin
                        // to those in the adjacent bin
                        for( Star star1 : bin ) for( Star star2 : newbin )
                        {
                            if( star1.d2( star2 ) < kk ) ++count;
                        }
                    }
                }
             }
            
            ps.println( count );
        }
    }
    
    /**
     * @param args
     */
    public static void main( String[] args ) throws Exception
    {
        new stars_vanb().doit();         
    }   
}
